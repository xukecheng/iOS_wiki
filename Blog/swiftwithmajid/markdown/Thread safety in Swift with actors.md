##  Thread safety in Swift with actors

19 Sep 2023

Actors is the new Swift language feature, making your types thread-safe. This
week, we will learn how to use actors and their benefits over locks. We will
also discuss actor reentrancy, the main confusing point of using actors.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In the previous post, we modeled a _Store_ type, allowing us to implement
state management predictably.

    
    
    @dynamicMemberLookup final class Store<State, Action> {
        typealias Reduce = (State, Action) -> State
        
        private var state: State
        private let reduce: Reduce
        
        init(state: State, reduce: @escaping Reduce) {
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
    

At this point, the _Store_ type is not thread-safe, and using it from multiple
threads may lead to data races and race conditions. We solve the issue by
using an instance of the _NSRecursiveLock_ type.

    
    
    @dynamicMemberLookup final class Store<State, Action> {
        typealias Reduce = (State, Action) -> State
        
        private var state: State
        private let reduce: Reduce
        
        private let lock = NSRecursiveLock()
        
        init(state: State, reduce: @escaping Reduce) {
            self.state = state
            self.reduce = reduce
        }
        
        subscript<T>(dynamicMember keyPath: KeyPath<State, T>) -> T {
            lock.withLock {
                state[keyPath: keyPath]
            }
        }
        
        func send(_ action: Action) {
            lock.withLock {
                state = reduce(state, action)
            }
        }
    }
    

As you can see in the example above, we use an instance of the
_NSRecursiveLock_ type whenever we access the protected part of the store. We
made our store thread-safe, but let me tell you about a few downsides of using
locks.

First, you must wrap every use of the state property with the _withLock_
function. Whenever you miss it accidentally or not, the _Store_ type is not
thread-safe anymore. So, you should be very careful while using locks.

Second, when you call the _lock_ or _withLock_ functions, they completely hang
the current thread until the lock is released, which may lead to performance
issues when many threads access the protected value.

> To learn more about locks in Swift, take a look at my [ “Thread safety in
> Swift with locks” ](/2023/09/05/thread-safety-in-swift-with-locks/) post.

Swift language introduced a feature called actors to solve these complex
issues. Actors like classes are reference types but protect their stored
properties from multithread access.

    
    
    @dynamicMemberLookup actor Store<State, Action> {
        typealias Reduce = (State, Action) -> State
        
        private var state: State
        private let reduce: Reduce
        
        init(state: State, reduce: @escaping Reduce) {
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
    

As you can see in the example above, we define our Store type by using
**actor** keyword instead of _class_ . That’s all you need to make your
_Store_ thread-safe. Actor isolation guarantees exclusive access to the stored
fields of an actor type. You must use the **await** keyword to access property
or function on an actor type.

    
    
    final class StoreTests: XCTestCase {
        struct State {
            var value = 0
        }
        
        func testThreadSafety() async {
            let store = Store<State, Void>(state: .init()) { state, _ in
                var state = state
                state.value += 1
                return state
            }
            
            await withTaskGroup(of: Void.self) { group in
                for _ in 0..<1_000_000 {
                    group.addTask {
                        await store.send(())
                    }
                }
            }
            
            let value = await store.value
            
            XCTAssertEqual(value, 1_000_000)
        }
    }
    

The _await_ keyword is part of the Swift Concurrency feature, allowing us to
await the results whenever we switch threads. In the example above, we use
_await_ on every touch to the actor because another thread might use the
actor, and we must wait for our exclusive access. Swift Compiler guarantees
exclusive access, and we have compile-time verification on thread safety.

    
    
    @dynamicMemberLookup actor Store<State, Action> {
        typealias Reduce = (State, Action) -> State
        typealias Intercept = (State, Action) async -> Action?
        
        private var state: State
        private let reduce: Reduce
        private let intercept: Intercept
        
        init(
            state: State,
            reduce: @escaping Reduce,
            intercept: @escaping Intercept
        ) {
            self.state = state
            self.reduce = reduce
            self.intercept = intercept
        }
        
        subscript<T>(dynamicMember keyPath: KeyPath<State, T>) -> T {
            state[keyPath: keyPath]
        }
        
        func send(_ action: Action) async {
            state = reduce(state, action)
            
            if let nextAction = await intercept(state, action) {
                await send(nextAction)
            }
        }
    }
    

Now let’s talk about actor reentrancy. What if we run async code on an actor?
In this case, the actor suspends execution and switches threads to run an
async function outside the actor. During this time, the actor allows other
threads access its isolated properties and functions because it doesn’t run
the async code itself. When the async code finishes, the actor switches back
to run actor-isolated code.

Remember that every use of the _await_ keyword inside an actor type is a
possible suspension point where other threads may access or mutate actor-
isolated properties. This situation is called actor reentrancy. You may have
race conditions during actor reentrancy if you assume that actors always run
code atomically.

Today we learned about another great feature of Swift language. In general, I
suggest to use actors by default and switch to locks only when you need thread
safety outside of async context. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and happy multithreading!

