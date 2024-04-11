##  The power of task view modifier in SwiftUI

28 Jun 2022

_Task_ view modifier is the key to the Swift Concurrency world through
SwiftUI. It allows us to build complex async tasks by leveraging the power of
cooperative cancellation and the lifecycle of a SwiftUI view. This week we
will learn all the powerful features of the _task_ view modifier in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        
        var body: some View {
            NavigationStack {
                List(store.products) { product in
                    NavigationLink {
                        Text(product.id.uuidString)
                    } label: {
                        Text(product.id.uuidString)
                    }
                }
                .task {
                    await store.fetchProducts()
                }
            }
        }
    }
    

The _task_ view modifier starts the unstructured async task and binds it to
the view lifecycle. SwiftUI automatically cancels ongoing tasks whenever the
view disappears by propagating cooperative cancellation.

    
    
    @MainActor final class Store: ObservableObject {
        @Published private(set) var products: [Product] = [
            .init(), .init(), .init()
        ]
        
        func fetchProducts() async {
            do {
                try await Task.sleep(nanoseconds: 3_000_000_000)
                products = [.init(), .init(), .init()]
            } catch {
                // Ignore CancellationError
            }
        }
    }
    

As you can see in the example above, we pause the task by using the _sleep_
function that throws _CancellationError_ whenever a task is canceled during
the sleep. Alternatively, you can use the _isCancelled_ property on the _Task_
type indicating whether or not the current task is canceled.

By default, the _task_ view modifier uses the user-initiated (highest)
priority for the created task, but you can also use lower preferences like
utility or background.

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        
        var body: some View {
            NavigationStack {
                List(store.products) { product in
                    NavigationLink {
                        Text(product.id.uuidString)
                    } label: {
                        Text(product.id.uuidString)
                    }
                }
                .task(priority: .utility) {
                    await store.fetchProducts()
                }
            }
        }
    }
    

Another variant of the _task_ view modifier allows us to observe equitable
data and run the async task whenever the data changes. The task lifecycle is
still bound to the view lifecycle, but SwiftUI also cancels the ongoing job
whenever data changes and creates a new one for the latest data.

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        @State private var query = ""
        
        var body: some View {
            NavigationStack {
                List(store.products) { product in
                    NavigationLink {
                        Text(product.id.uuidString)
                    } label: {
                        Text(product.id.uuidString)
                    }
                }
                .searchable(text: $query)
                .task(id: query) {
                    await store.search(matching: query)
                }
            }
        }
    }
    

> To learn more about building search functionality in SwiftUI, take a look at
> my [ “Mastering search in SwiftUI” ](/2021/06/23/mastering-search-in-
> swiftui/) post.

In the example above, whenever the user types the query in the search bar
SwiftUI creates a task. SwiftUI makes a task for every change in the search
query in this case. Usually, we want to debounce requests to our servers and
make them after a slight pause. We can quickly achieve this effect by
leveraging the power of the cooperative cancellation and data observing
capabilities of the _task_ view modifier.

    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        @State private var query = ""
        
        var body: some View {
            NavigationStack {
                List(store.products) { product in
                    NavigationLink {
                        Text(product.id.uuidString)
                    } label: {
                        Text(product.id.uuidString)
                    }
                }
                .searchable(text: $query)
                .task(id: query) {
                    do {
                        try await Task.sleep(nanoseconds: 300_000_000)
                        await store.search(matching: query)
                    } catch {
                        // Task cancelled without network request.
                    }
                }
            }
        }
    }
    

Here we try to sleep for a bit and make a network query only if the user
doesn’t type a new query. In another case, SwiftUI cancels the task and
creates a new one.

    
    
    struct DebouncingTaskViewModifier<ID: Equatable>: ViewModifier {
        let id: ID
        let priority: TaskPriority
        let nanoseconds: UInt64
        let task: @Sendable () async -> Void
        
        init(
            id: ID,
            priority: TaskPriority = .userInitiated,
            nanoseconds: UInt64 = 0,
            task: @Sendable @escaping () async -> Void
        ) {
            self.id = id
            self.priority = priority
            self.nanoseconds = nanoseconds
            self.task = task
        }
        
        func body(content: Content) -> some View {
            content.task(id: id, priority: priority) {
                do {
                    try await Task.sleep(nanoseconds: nanoseconds)
                    await task()
                } catch {
                    // Ignore cancellation
                }
            }
        }
    }
    
    extension View {
        func task<ID: Equatable>(
            id: ID,
            priority: TaskPriority = .userInitiated,
            nanoseconds: UInt64 = 0,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            modifier(
                DebouncingTaskViewModifier(
                    id: id,
                    priority: priority,
                    nanoseconds: nanoseconds,
                    task: task
                )
            )
        }
    }
    

Debouncing via _task_ view modifier becomes very handy in my projects. That’s
why I created a small wrapper around the _task_ view modifier, allowing us to
debounce tasks without this boilerplate.

> To learn more about building custom view modifiers, take a look at my [
> “ViewModifiers in SwiftUI” ](/2019/08/07/viewmodifiers-in-swiftui/) post.
    
    
    struct ContentView: View {
        @StateObject private var store = Store()
        @State private var query = ""
        
        var body: some View {
            NavigationStack {
                List(store.products) { product in
                    NavigationLink {
                        Text(product.id.uuidString)
                    } label: {
                        Text(product.id.uuidString)
                    }
                }
                .searchable(text: $query)
                .task(id: query, nanoseconds: 300_000_000) {
                    await store.search(matching: query)
                }
            }
        }
    }
    

Today we learned how to use the _task_ view modifier and the different
opportunities it provides to handle complex async flows. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

