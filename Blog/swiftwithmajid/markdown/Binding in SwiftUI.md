##  Binding in SwiftUI

08 Apr 2020

Binding is one of the several property wrappers that SwiftUI presents us to
control data flow in the app. Binding provides us a reference like access to a
value type. This week we will understand how and when to use binding. We will
learn how to avoid common mistakes while using binding in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Binding is a property wrapper type that can read and write a value owned by a
source of truth. We have several possible types of sources of truth in
SwiftUI. It can be _EnvironmentObject_ , _ObservedObject_ or _State_ . All
these property wrappers provide a projected value, which is binding. Let’s
take a look at the quick example.

    
    
    import SwiftUI
    
    struct ExampleView: View {
        @State private var text = "Hello World."
    
        var body: some View {
            TextField("type something...", text: $text)
        }
    }
    

Here we have a state that is a source of truth. We also have a _TextField_ ,
which requires a binding for a text value. We use a _dollar sign_ to access
the projected value of the state property wrapper, which is a binding to the
value of property wrapper.

> To learn more about property wrappers in SwiftUI, take a look at my [
> “Understanding Property Wrappers in SwiftUI” post
> ](/2019/06/12/understanding-property-wrappers-in-swiftui/) .

####  Common mistakes

Let’s take a look at the more complicated example. We will build an app that
shows the list of users and allows us to edit user data.

    
    
    import SwiftUI
    import Combine
    
    struct Person: Identifiable {
        let id: UUID
        var name: String
        var age: Int
    }
    
    final class PersonStore: ObservableObject {
        @Published var persons: [Person] = [
            .init(id: .init(), name: "Majid", age: 28),
            .init(id: .init(), name: "John", age: 31),
            .init(id: .init(), name: "Fred", age: 25)
        ]
    }
    
    struct PersonsView : View {
        @ObservedObject var store: PersonStore
    
        var body: some View {
            NavigationView {
                List {
                    ForEach($store.persons) { $person in
                        NavigationLink(destination: EditingView(person: $person)) {
                            VStack(alignment: .leading) {
                                Text(person.name)
                                    .font(.headline)
                                Text("Age: \(person.age)")
                                    .font(.subheadline)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }
                }.navigationBarTitle(Text("Persons"))
            }
        }
    }
    

Take a look at how we generate bindings inside _ForEach_ view. We use **$**
sign to define closure parameter and it automatically generates binding for
us.

Please keep in mind that the value of binding must be a value type. It means
it has to be an enum or a struct. I see that people sometimes use classes to
describe a state or entry inside _EnvironmentObject_ or _ObservedObject_ and
notice that binding is not working. Apple’s documentation on binding says: if
_Value_ is not value semantic, the updating behavior for any views that make
use of the resulting _Binding_ is unspecified.

    
    
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
    

As you can see in the example above, we use binding to pass a writable
reference to a person struct. As soon as we modify the user instance inside
the _EditingView_ SwiftUI updates _PersonsView_ to respect the changes.

> To learn more about building editable forms using _Form_ component, take a
> look at my [ “Building forms with SwiftUI” ](/2019/06/19/building-forms-
> with-swiftui/) post.

####  Computed Binding

Usually, we access binding using a projected value of a source of truth. In
this section, we will talk about another way of creating a binding. Binding is
a two-way connection between the data and a view that access it. SwiftUI
provides a way to construct a binding using getter and setter closures. In
this case, we are responsible for calculating the value inside these closures.
It is hard to imagine where we can use it, but it plays very well with Redux-
like state containers.

    
    
    typealias Reducer<State, Action> = (inout State, Action) -> Void
    
    final class Store<State, Action>: ObservableObject {
        @Published private(set) var state: State
        private let reducer: Reducer<State, Action>
    
        init(initialState: State, reducer: Reducer<State, Action>) {
            self.state = initialState
            self.reducer = reducer
        }
    
        func send(_ action: Action) {
            reducer(&state, action)
        }
    }
    

Here we have a concept of store that holds the entire state of the app. All
changes to the state come from the unidirectional flow. Reducer is the single
place where we can mutate the state of the app. By using computed binding, we
can provide read-only access to the state and respect the unidirectional flow
by sending action to the reducer.

    
    
    extension Store {
        func binding<Value>(
            for keyPath: KeyPath<State, Value>,
            transform: @escaping (Value) -> Action
        ) -> Binding<Value> {
            Binding<Value>(
                get: { self.state[keyPath: keyPath] },
                set: { self.send(transform($0)) }
            )
        }
    }
    

As you can see, we generate a computed binding that reads a part of the state
and emits an action through reducer to modify the state when needed. You might
need this type of bindings when you, for example, have a settings screen that
describes some checkboxes bound to the app state.

> To learn more about implementing Redux in SwiftUI, take a look at my [
> “Redux-like state container in SwiftUI” post ](/2019/09/18/redux-like-state-
> container-in-swiftui/) .

####  Constant binding

Another way to create binding is the _static constant_ function. This function
allows us to create a binding that provides value but ignores any mutations on
it. In other words, it generates an immutable binding for provided value.

    
    
    import SwiftUI
    
    struct ExampleView: View {
        var body: some View {
            TextField("type something...", text: Binding.constant("Hello!"))
        }
    }
    

####  Conclusion

Today we learned another great tool to control data flow in SwiftUI. Binding
can be a tool which is more complicated than others, but I believe we cover
all the needed things for efficient use of bindings in SwiftUI. I hope you
enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

