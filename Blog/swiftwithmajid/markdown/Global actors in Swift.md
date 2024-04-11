##  Global actors in Swift

12 Mar 2024

The Swift language allows us to define thread-safe types using actors. Actor
type automatically manages serial access to the data it protects. But what if
we need multiple types protected by a single serial access queue? That’s why
we have global actors, and today, we will learn how to use global actors in
Swift.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The main thread rendering is the best example of why we need to protect
multiple types with a single serial access queue. You may have a massive
collection of _UIViewControllers_ , _UIViews_ , or SwiftUI views running
concurrently, but in the end, you should update your user interface on the
serial main thread.

> If you are unfamiliar with the actor concept, look at my dedicated [ “Thread
> safety in Swift with actors” ](/2023/09/19/thread-safety-in-swift-with-
> actors/) post.

That’s why Swift provides us _@MainActor_ . Any _UIViewController_ or _UIView_
you create inherits _@MainActor_ access from its definition. SwiftUI’s _View_
protocol also defines its _body_ property with _@MainActor_ . This means your
view’s body, view, or controller always runs on the main thread and protects
you from accidentally updating the user interface from the background thread.

To fully understand the idea of the global actors, let’s inspect the
_@MainActor_ type a bit further.

    
    
    @globalActor actor MainActor : GlobalActor {
        static let shared: MainActor
    }
    

As you can see in the code example above, the _MainActor_ type is defined with
**actor** keyword and conforms to the _GlobalActor_ protocol. It also has the
**@globalActor** attribute. The _GlobalActor_ protocol requires you to specify
the _shared_ property to create a shared, also called a global instance of the
actor.

    
    
    @Observable @MainActor final class Store {
        // ...
    }
    

Now, we can easily mark any type we need with the _@MainActor_ attribute to
isolate it to the main actor. This means all the work in the particular type
runs serially on the main actor.

Let’s move forward and build our own global actor. Assume that you have a set
of types accessing the local storage and you want to keep files conflict-free
on the disk by running only in a serial order.

    
    
    @globalActor actor StorageActor: GlobalActor {
        static let shared = StorageActor()
    }
    

As you can see in the example above, we define the _StorageActor_ type
conforming to the _GlobalActor_ protocol using the **actor** keyword. The
_@globalActor_ attribute allows us to mark any type, function, or property
with the _@StorageActor_ .

    
    
    @StorageActor final class Cache {
        let folder: URL
        
        init(folder: URL) {
            self.folder = folder
        }
        
        func get(_ key: String) -> Data? {
            // ...
        }
        
        func set(data: Data, for key: String) {
            // ...
        }
    }
    
    @StorageActor final class Database<Value> {
        let folder: URL
        
        init(folder: URL) {
            self.folder = folder
        }
        
        func search(matching query: String) -> [Value] {
            // ...
        }
    }
    

Here, we create _Сache_ and _Database_ types using the _@StorageActor_
attribute. It allows us to run them on a shared serial queue managed by the
_StorageActor_ we created before.

Why do we use global actors rather than defining _Cache_ and _Database_ types
as actors? We can define _Cache_ and _Database_ as actors. Still, in this
case, every instance of the _Cache_ or _Database_ types will run on an
independent serial queue and protect its access alone. By marking our types
with the _@StorageActor_ , we belong them to a single serial queue managed by
the shared instance of the _StorageActor_ .

    
    
    @Observable final class Store {
        private(set) var data: Data?
        
        @StorageActor func load() async {
            let path: String = "some path"
            let content = FileManager.default.contents(atPath: path)
            
            await MainActor.run {
                self.data = content
            }
        }
    }
    

Remember that you can mark with the _@StorageActor_ attribute not only types
but also functions or properties of any type.

Today, we learned why and how to use global actors in Swift. You don’t need to
use global actors often in your apps. However, they become handy in particular
cases, such as main thread rendering. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

