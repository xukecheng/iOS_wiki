##  Modeling app state using Store objects in SwiftUI

04 Sep 2019

This week I want to talk to you about modeling data layer in SwiftUI. I
already finished work on my very first app, which I build entirely with
SwiftUI. And now I can share with you the way of architecting model layer
using store objects which I used during the development of _NapBot_ .

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Store object

Store objects responsible for storing the state and providing actions to
mutate that state. You can have as many store objects as you need to keep them
simple and responsible for a small part of your app state. For example, you
may have _SettingsStore_ to keep a state of user-defined settings and
_TodoStore_ to keep user tasks.

To create a store object, we need a class which conforms to _ObservableObject_
. _ObservableObject_ allows SwiftUI to observe and react to data changes.
Let’s take a look at a simple example of _SettingsStore_ object.

> To learn more about _ObservableObject_ , take a look at [ “Managing Data
> Flow in SwiftUI” ](/2019/07/03/managing-data-flow-in-swiftui/) post.
    
    
    import Foundation
    import Combine
    
    final class SettingsStore: ObservableObject {
        let objectWillChange = PassthroughSubject<Void, Never>()
    
        @UserDefault(Constants.UserDefaults.sleepGoal, defaultValue: 8.0)
        var sleepGoal: Double
    
        @UserDefault(Constants.UserDefaults.notifications, defaultValue: true)
        var isNotificationsEnabled: Bool
    
        private var didChangeCancellable: AnyCancellable?
    
        override init() {
            super.init()
            didChangeCancellable = NotificationCenter.default
                .publisher(for: UserDefaults.didChangeNotification)
                .map { _ in () }
                .receive(on: DispatchQueue.main)
                .subscribe(objectWillChange)
        }
    }
    

In the code sample above, we have _SettingsStore_ class which provides access
to the user-defined settings. We also use _didChangeNotification_ to notify
SwiftUI whenever user defaults changes.

####  Advanced usage

Let’s take a look at another usage of the store object by creating a simple
Todo app. We need to create a store object which stores the list of tasks and
provides actions to mutate them like deleting and filtering.

    
    
    import Foundation
    import Combine
    
    struct Todo: Identifiable, Hashable {
        let id = UUID()
        var title: String
        var date: Date
        var isDone: Bool
        var priority: Int
    }
    
    final class TodosStore: ObservableObject {
        @Published var todos: [Todo] = []
    
        func orderByDate() {
            todos.sort { $0.date < $1.date }
        }
    
        func orderByPriority() {
            todos.sort { $0.priority > $1.priority }
        }
    
        func removeCompleted() {
            todos.removeAll { $0.isDone }
        }
    }
    

Here we have a _TodosStore_ class which conforms to _ObservableObject_
protocol. _TodosStore_ provides few actions to mutate its state, we can use
these methods from our views. By default, SwiftUI updates the views whenever @
_Published_ field changes. That’s why we marked our array of _Todo_ items as @
_Published_ . As soon as we insert or remove items from that array, SwiftUI
will update views subscribed to the _TodosStore_ .

Now, we can create a view which represents the list of tasks and provides
actions like marking a task as completed, deleting, and reordering. Let’s
start by creating a view which shows the title of the task and a toggle to
mark the task as completed.

    
    
    import SwiftUI
    
    struct TodoItemView: View {
        let todo: Binding<Todo>
    
        var body: some View {
            HStack {
                Toggle(isOn: todo.isDone) {
                    Text(todo.title.wrappedValue)
                        .strikethrough(todo.isDone.wrappedValue)
                }
            }
        }
    }
    

In the example above, we use _Binding_ to provide a reference like access to a
value type. In other words, we provide writable access to a todo item.
_TodoItemView_ doesn’t own an instance of _Todo_ struct, but it has writable
access to the _TodoStore_ via _Binding_ .

    
    
    import SwiftUI
    
    struct TodosView: View {
        @EnvironmentObject var store: TodosStore
        @State private var draft: String = ""
    
        var body: some View {
            NavigationView {
                List {
                    TextField("Type something...", text: $draft, onCommit: addTodo)
                    ForEach(store.todos.indexed(), id: \.1.id) { index, _ in
                        TodoItemView(todo: self.$store.todos[index])
                    }
                    .onDelete(perform: delete)
                    .onMove(perform: move)
                }
                .navigationBarItems(trailing: EditButton())
                .navigationBarTitle("Todos")
            }
        }
    
        private func delete(_ indexes: IndexSet) {
            store.todos.remove(atOffsets: indexes)
        }
    
        private func move(_ indexes: IndexSet, to offset: Int) {
            store.todos.move(fromOffsets: indexes, toOffset: offset)
        }
    
        private func addTodo() {
            let newTodo = Todo(title: draft, date: Date(), isDone: false, priority: 0)
            store.todos.insert(newTodo, at: 0)
            draft = ""
        }
    }
    

Here we have a _TodosView_ which uses _List_ component to represent todos.
_List_ component also provides reorder and delete actions. Another interesting
thing here is _indexed_ () function. This function returns a collection of
items with its indexes. We use it to access store items via Binding. Here is a
full source of this extension.

    
    
    import Foundation
    
    struct IndexedCollection<Base: RandomAccessCollection>: RandomAccessCollection {
        typealias Index = Base.Index
        typealias Element = (index: Index, element: Base.Element)
    
        let base: Base
    
        var startIndex: Index { base.startIndex }
    
        var endIndex: Index { base.endIndex }
    
        func index(after i: Index) -> Index {
            base.index(after: i)
        }
    
        func index(before i: Index) -> Index {
            base.index(before: i)
        }
    
        func index(_ i: Index, offsetBy distance: Int) -> Index {
            base.index(i, offsetBy: distance)
        }
    
        subscript(position: Index) -> Element {
            (index: position, element: base[position])
        }
    }
    
    extension RandomAccessCollection {
        func indexed() -> IndexedCollection<Self> {
            IndexedCollection(base: self)
        }
    }
    

The environment is a perfect candidate to keep store objects. Environment can
share it between multiple views without explicit injection via init method.

> To learn more about the benefits of _Environment_ in SwiftUI, take a look at
> [ “The power of Environment in SwiftUI” ](/2019/08/21/the-power-of-
> environment-in-swiftui/) post.

![todos-screenshots](/public/todo.jpeg)

####  Conclusion

Today we talked about the way of modeling app state by using multiple store
objects. I really enjoy the simplicity of this approach and how easily you can
scale your app by injecting more store objects into the environment. I hope
you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

