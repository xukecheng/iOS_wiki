##  Submitting values to SwiftUI view

21 Jul 2021

SwiftUI Release 3 brought us a new declarative approach for handling submitted
values. Text fields, forms, search bars allow users to submit values that we
can take and react to them using the new _onSubmit_ view modifier. This week
we will learn how to use the _onSubmit_ view modifier and what benefits it
provides us.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Let’s build a view that allows us to search for messages using the
_searchable_ view modifier.

    
    
    struct SearchView: View {
        @ObservedObject var viewModel: ViewModel
        @Binding var query: String
    
        var body: some View {
            List(viewModel.messages, id: \.self) { message in
                Text(message)
            }
            .searchable(text: $query)
            .onSubmit(of: .search) {
                viewModel.search(matching: query)
            }
            .navigationTitle("Search")
        }
    }
    

As you can see in the example above, we display the list of messages from
_ViewModel_ and provide the search functionality. We also use the _onSubmit_
view modifier to provide a closure that SwiftUI runs whenever the user submits
the value. As soon as the user hits the return key on the software or hardware
keyboard, SwiftUI calls the provided closure.

> To learn more about using the search view modifier, take a look at my [
> “Mastering search in SwiftUI” ](/2021/06/23/mastering-search-in-swiftui/)
> post.

We use the _onSubmit_ view modifier with a search submit trigger. It means
SwiftUI runs the given closure only as a result of search action. SwiftUI
provides us a set of different submit triggers like _search, text, form,_ and
its count can increase in the future releases of SwiftUI.

Other views which we can use in conjunction with the _onSubmit_ view modifier
are _TextField_ and _SecureField_ . We can attach the _onSubmit_ view modifier
directly to the text field. In this case, we have to use the text submit
trigger.

    
    
    struct ContentView: View {
        @State private var query = ""
    
        var body: some View {
            NavigationView {
                TextField("query", text: $query)
                    .onSubmit(of: .text) {
                        print(query)
                    }
            }
        }
    }
    

Keep in mind that we can attach multiple _onSubmit_ view modifiers with
various submit triggers to the view hierarchy and provide different closures
for separate triggers.

We can also change the label of the return key on the software keyboard using
the _submitLabel_ view modifier. _submitLabel_ view modifier requires the
instance of _SubmitLabel_ struct as the parameter which defined the return key
label. It has many predefined values like _done, go, send, join, route,
search, return, next and continue._

    
    
    struct ContentView: View {
        @State private var query = ""
    
        var body: some View {
            NavigationView {
                TextField("query", text: $query)
                    .submitLabel(.send)
                    .onSubmit(of: .text) {
                        print(query)
                    }
            }
        }
    }
    

####  Scopes

I should mention that you can place the _onSubmit_ view modifier not only
under text fields, but it can be anywhere in the view hierarchy. That’s why
SwiftUI provides us an opportunity to control submit scopes. For example, you
can disable a part of the view hierarchy to react on submitting values.

    
    
    struct ContentView: View {
        @StateObject private var viewModel = ViewModel()
    
        var body: some View {
            NavigationView {
                VStack {
                    TextField("phone", text: $viewModel.phone)
                        .submitScope(viewModel.phone.count > 11)
    
                    VStack {
                        TextField("email", text: $viewModel.email)
                        TextField("password", text: $viewModel.password)
                    }
                }
                .onSubmit(of: .text) {
                    viewModel.signUp()
                }
            }
        }
    }
    

The _submitScope_ view modifier allows you to avoid specific views from
invoking a submission action. In our example, the phone text field will not
initiate a submission while the provided condition is false.

####  Conclusion

This week, we learned about the new _onSubmit_ view modifier that provides us
with a generic way to handle the value submission for different views. I hope
you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

