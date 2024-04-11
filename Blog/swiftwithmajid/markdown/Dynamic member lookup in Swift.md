##  Dynamic member lookup in Swift

23 May 2023

One of my favorite features of the Swift Language is the dynamic member
lookup. We don’t use it very often, but it improves the API of the provided
type significantly by improving the way we access the data of the particular
type.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Assume that we are working on a type providing caching functionality, and we
model it as the struct called _Cache_ .

    
    
    struct Cache {
        var storage: [String: Data] = [:]
    }
    

To access cached data, we call the subscript of the storage property that the
_Dictionary_ type provides us.

    
    
    var cache = Cache()
    let profile = cache.storage["profile"]
    

Nothing is exceptional here. We access the dictionary as we used by using the
subscript of the _Dictionary_ type. Let’s look at how we can improve the API
of the _Cache_ type using the _@dynamicMemberLookup_ attribute.

    
    
    @dynamicMemberLookup
    struct Cache {
        private var storage: [String: Data] = [:]
        
        subscript(dynamicMember key: String) -> Data? {
            storage[key]
        }
    }
    

As you can see in the example above, we mark our _Cache_ type with the
_@dynamicMemberLookup_ attribute. We must implement the subscript with the
_dynamicMember_ parameter returning anything we need.

    
    
    var cache = Cache()
    let profile = cache.profile
    

Now, we can access the profile data of our _Cache_ type more nicely. The user
of our API may assume that the _profile_ is the property of the _Cache type_ .
But it is not.

This feature works completely in runtime and leverages the name of any
property we type after the dot symbol to the subscript of the _Cache_ type
with the _dynamicMember_ parameter.

The whole logic runs in runtime, and the result is undefined during
compilation. It is entirely up to you to decide which data you should return
from the subscript during runtime and how you want to handle the
_dynamicMember_ parameter.

####  Compile-time safety with KeyPath

The only downside we can find is the absence of compile-time safety. We can
treat the _Cache_ type as if it has any property name we type in the code.
Fortunately, the parameter of the _@dynamicMemberLookup_ subscript may be not
only String-typed but also _KeyPath_ .

    
    
    @dynamicMemberLookup
    final class Store<State, Action>: ObservableObject {
        typealias ReduceFunction = (State, Action) -> State
        
        @Published private var state: State
        private let reduce: ReduceFunction
        
        init(
            initialState state: State,
            reduce: @escaping ReduceFunction
        ) {
            self.state = state
            self.reduce = reduce
        }
        
        subscript<T>(dynamicMember keyPath: KeyPath<State, T>) -> T {
            state[keyPath: keyPath]
        }
        
        func send(_ action: Action) {
            state = reduce(state, action)
        }
    }
    

As you can see in the example above, we define the subscript with the
_dynamicMember_ parameter accepting an instance of the strong-typed _KeyPath_
. In this case, we allow _KeyPath_ of the _State_ type, which helps us to have
compile-time safety. Because the compiler will show an error anytime we pass a
wrong _KeyPath_ , which is not connected to the _State_ type.

    
    
    struct State {
        var products: [String] = []
        var isLoading = false
    }
    
    enum Action {
        case fetch
    }
    
    let store: Store<State, Action> = .init(initialState: .init()) { state, action in
        var state = state
        switch action {
        case .fetch:
            state.isLoading = true
        }
        return state
    }
    
    
    print(store.isLoading)
    print(store.products)
    print(store.favorites) // Compiler error
    

In the example above, we access the private _state_ property of the _Store_
using the subscript accepting the _KeyPath_ . It looks similar to the previous
example, but in this case, the compiler shows an error whenever you try to
access an unavailable property of the _State_ type.

Today we learned how to improve the API of a particular type by using the
_@dynamicMemberLookup_ attribute. You don’t need it in every type, but you can
use it carefully to improve the API. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

