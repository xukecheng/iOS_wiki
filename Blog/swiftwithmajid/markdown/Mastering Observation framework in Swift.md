##  Mastering Observation framework in Swift

03 Oct 2023

Apple introduced the new Observation framework powered by the macro feature of
the Swift language. The new Observation framework, in combination with the
Swift Concurrency features, allows us to replace the Combine framework that
looks deprecated by Apple. This week, we will learn how to use the Observation
framework to handle data flow in our apps.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Using the new Observation Framework is super easy. All you need to do is to
mark your class with the **@Observable** macro.

    
    
    @Observable final class Store<State, Action> {
        typealias Reduce = (State, Action) -> State
        
        private(set) var state: State
        private let reduce: Reduce
        
        init(initialState state: State, reduce: @escaping Reduce) {
            self.state = state
            self.reduce = reduce
        }
        
        func send(_ action: Action) {
            state = reduce(state, action)
        }
    }
    

As you can see in the example above, we use the _@Observable_ macro to
annotate our _Store_ type. After that, we can observe any variable in the
_Store_ type. We have only one variable in the _Store_ type that defines the
store’s state. Another field is a _let_ constant that never changes.

    
    
    withObservationTracking {
        render(store.state)
    } onChange: {
        print("State changed")
    }
    

To observe an instance of the _Store_ type, we need to call the
_withObservationTracking_ function with two closures. In the first closure, we
can touch all the needed properties of the observable type. The Observation
framework calls the second closure only once as soon as any touched property
of the observed type changes.

    
    
    func startObservation() {
        withObservationTracking {
            render(store.state)
        } onChange: {
            Task { startObservation() }
        }
    }
    

The Observation framework runs the _onChange_ only once, which means you
should call it recursively to observe changes constantly. Another thing you
should be aware of is that _onChange_ closure runs before the actual change
applies. That’s why we postpone the _onChange_ action by starting a new task.

In SwiftUI, you don’t need to use the _withObservationTracking_ function to
observe changes. SwiftUI automatically tracks changes of any observable type’s
property used inside the view body.

    
    
    struct ProductsView: View {
        let store: Store<AppState, AppAction>
        
        var body: some View {
            List(store.state.products, id: \.self) { product in
                Text(product)
            }
            .onAppear {
                store.send(.fetch)
            }
        }
    }
    

As you can see in the example above, we don’t use any property wrappers to
observe the store. SwiftUI does it automatically. As soon as the state
property of the store changes, SwiftUI updates the view. We don’t need the
_@ObservedObject_ property wrapper to track changes in observable types, but
we still need the _@StateObject_ alternative to survive through the SwiftUI
lifecycle.

Apple simplifies the set of property wrappers we should use with the new
Observation framework. Instead of the _@StateObject_ property wrapper, we can
use _@State_ now. _@State_ property wrapper works for simple value types and
any observable types now.

    
    
    struct ContentView: View {
        @State private var store = Store<AppState, AppAction>(
            initialState: .init(),
            reduce: reduce
        )
        
        var body: some View {
            ProductsView(store: store)
        }
    }
    

The same approach goes to the environment feature of the SwiftUI framework.
There is no need for the _@EnvironmentObject_ property wrapper now. You can
now use the _@Environment_ property wrapper and the _environment_ view
modifier with observable types.

    
    
    struct ContentView: View {
        @State private var store = Store<AppState, AppAction>(
            initialState: .init(),
            reduce: reduce
        )
        
        var body: some View {
            ProductsView()
                .environment(store)
        }
    }
    
    struct ProductsView: View {
        @Environment(Store<AppState, AppAction>.self) var store
        
        var body: some View {
            List(store.state.products, id: \.self) { product in
                Text(product)
            }
            .onAppear {
                store.send(.fetch)
            }
        }
    }
    

The last thing you may wonder is how to derive a binding from an observable
type. SwiftUI introduces a _@Bindable_ property wrapper for this case that
works only with observable types.

    
    
    @Observable final class AuthViewModel {
        var username = ""
        var password = ""
        
        var isAuthorized = false
        
        func authorize() {
            isAuthorized.toggle()
        }
    }
    
    struct AuthView: View {
        @Bindable var viewModel: AuthViewModel
        
        var body: some View {
            VStack {
                if !viewModel.isAuthorized {
                    TextField("username", text: $viewModel.username)
                    SecureField("password", text: $viewModel.password)
                    
                    Button("authorize") {
                        viewModel.authorize()
                    }
                } else {
                    Text("Hello, \(viewModel.username)")
                }
            }
        }
    }
    

You can use the _@Bindable_ property wrapper to create bindings from the
properties of any observable type easily. Sometimes, you may need to inline
_@Bindable_ inside the view body to create bindings.

    
    
    struct InlineAuthView: View {
        @Environment(AuthViewModel.self) var viewModel
        
        var body: some View {
            @Bindable var viewModel = viewModel
            
            VStack {
                if !viewModel.isAuthorized {
                    TextField("username", text: $viewModel.username)
                    SecureField("password", text: $viewModel.password)
                    
                    Button("authorize") {
                        viewModel.authorize()
                    }
                } else {
                    Text("Hello, \(viewModel.username)")
                }
            }
        }
    }
    

I love how the new Observation framework simplifies the data flow in SwiftUI.
I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

