##  Managing Data Flow in SwiftUI

03 Jul 2019

Last week we talked about [ “Animations and Transitions in SwiftUI”
](/2019/06/26/animations-in-swiftui/) . But it’s time to touch the crucial
aspect of every app, and it is _Data Flow_ . All the apps have data to present
or mutate. Data plays a vital role in apps using SwiftUI. Every view in
SwiftUI is just a function of some state, where the state is our data.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Fetching data from local/remote storage

Today we will build a small app which uses core SwiftUI concepts like
_Binding_ and _ObservableObject_ . Assume that you work on the app, which has
two primary responsibilities:

  1. Fetch and show the list of employees from local or remote storage 
  2. Edit personal information about selected employee 

Let’s start with describing our model layer.

    
    
    import SwiftUI
    import Combine
    
    struct Person: Identifiable {
        let id: UUID
        var name: String
        var age: Int
    }
    
    final class PersonStore: ObservableObject {
        @Published var persons: [Person] = [
            .init(id: .init(), name: "Majid", age: 27),
            .init(id: .init(), name: "John", age: 31),
            .init(id: .init(), name: "Fred", age: 25)
        ]
    }
    

Here we have simple _Person_ struct which conforms _Identifiable_ protocol.
The single requirement of _Identifiable_ is _Hashable_ _id_ field. We
implement it by defining _id_ as _UUID_ . We also can use _Int_ instead of
_UUID_ .

Next, we can implement _PersonStore_ class, which is providing data for our
view. _PersonStore_ type conforms to _ObservableObject_ it will allow SwiftUI
to refresh the view as soon as any of _@Published_ fields change.

Now let’s take a look at _PersonListView_ .

    
    
    struct PersonsView : View {
        @ObservedObject var store: PersonStore
    
        var body: some View {
            NavigationView {
                List(store.persons) { person in
                    VStack(alignment: .leading) {
                        Text(person.name)
                            .font(.headline)
                        Text("Age: \(person.age)")
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                    }
                }
            }.navigationBarTitle(Text("Persons"))
        }
    }
    

We use _List_ component to present an array of _Person_ structs. Every row in
_List_ contains _VStack_ with two _Text_ components representing the name and
age of a _Person_ . We call _fetch_ method on store object as soon as List
appears. As you remember, our _PersonStore_ object notifies SwiftUI about data
changes, and SwiftUI rebuilds the view to present new data.

####  Editing

Next step is creating a new view which allows us to edit personal information
of selected _Person_ . We will use _Form_ component to show nice form for data
entry. You can check [ “Building forms with SwiftUI” ](/2019/06/19/building-
forms-with-swiftui/) to learn more about _Form_ component and its advantages.
Let’s dive into code which represents editing view.

    
    
    struct EditingView: View {
        @Environment(\.presentationMode) var presentation
        @Binding var person: Person
    
        var body: some View {
            Form {
                Section(header: Text("Personal information")) {
                    TextField("type something...", text: $person.name)
                    Stepper(value: $person.age) {
                        Text("Age: \(person.age)")
                    }
                }
    
                Section {
                    Button("Save") {
                        self.presentation.wrappedValue.dismiss()
                    }
                }
            }.navigationBarTitle(Text(person.name))
        }
    }
    

Here we use _Binding_ for selected person item. _Binding Property Wrapper_
allows passing a reference to a value type. By using _Binding_ property,
_EditingView_ can read and mutate the _Person_ struct, but it doesn’t store a
copy of it. We use this _Binding_ to mutate value inside _PersonsStore_ and as
soon as we do that SwiftUI will update the view with the updated list of
_Persons_ . If you want to learn more about _Property Wrappers_ available in
SwiftUI like @ _Binding_ , @ _Environment_ , @ _EnvironmentObject_ ,
_@ObservedObject_ , please take a look at the [ “Understanding Property
Wrappers in SwiftUI” ](/2019/06/12/understanding-property-wrappers-in-
swiftui/) .

Now let’s refactor our _PersonsView_ to support editing by passing _Binding_
to a selected _Person_ inside _EditingView_ .

    
    
    import Foundation
    
    extension RandomAccessCollection {
        func indexed() -> Array<(offset: Int, element: Element)> {
            Array(enumerated())
        }
    }
    
    import SwiftUI
    
    struct PersonsView : View {
        @ObservedObject var store: PersonStore
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(store.persons.indexed(), id: \.1.id) { index, person in
                        NavigationLink(destination: EditingView(person: self.$store.persons[index])) {
                            VStack(alignment: .leading) {
                                Text(person.name)
                                    .font(.headline)
                                Text("Age: \(person.age)")
                                    .font(.subheadline)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }
                }
                .onAppear(perform: store.fetch)
                .navigationBarTitle(Text("Persons"))
            }
        }
    }
    

And here is the screenshot of our app, you can see how it looks. ![managing-
data-flow-in-swiftui](/public/managing-data-flow-in-swiftui.png)

####  Conclusion

Today we built simple Master-Detail flow in SwiftUI. I’ve tried to show the
power of _Bindings_ in SwiftUI. You don’t need to post notifications or
observe key-values to indicate changes in your User Interface, all you need is
using correct _Property Wrapper provided by SwiftUI_ . Again, if you want to
learn when and which one should be used, check out my [ post about Property
Wrappers in SwiftUI ](/2019/06/12/understanding-property-wrappers-in-swiftui/)
. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading and see you next week!

