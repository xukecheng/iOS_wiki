##  API availability in Swift

17 May 2023

WWDC is coming pretty soon, and we are going to use a bunch of new APIs. But
how to use new APIs available only for the latest version of iOS? This week we
will learn about availability conditions in Swift.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Swift provides **#available** attributes allowing us to check the availability
of the function. Here is a quick example.

    
    
    func foo() {
        if #available(iOS 16, *) {
            // Use new APIs
        } else {
            // Use old APIs
        }
    }
    

As you can see in the example above, we use the _#available_ attribute to
check if the current platform supports the APIs from iOS 16. We also can use
the _#unavailable_ attribute to check if the platform is unavailable.

    
    
    func foo() {
        if #unavailable(iOS 16) {
            // Use old APIs
        } else {
            // Use new APIs
        }
    }
    

We learned how to use the _#available_ attribute to check the platform
version. But how the API developer should define functions and types to
provide the availability information?

    
    
    extension View {
        @available(iOS 14, *)
        func backportedTask<Value: Equatable>(
            id: Value,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            if #available(iOS 15, macOS 12, *) {
                return self.task(id: id, task)
            } else {
                return self.onChange(of: id) { _ in
                    Task { await task() }
                }
            }
        }
    }
    

Swift allows us to use the **@available** attribute to provide information
about the platform that function or type needs to run. We can separate
different platforms by using commas.

    
    
    extension View {
        @available(iOS 14, macOS 12, *)
        func backportedTask<Value: Equatable>(
            id: Value,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            if #available(iOS 15, macOS 12, *) {
                return self.task(id: id, task)
            } else {
                return self.onChange(of: id) { _ in
                    Task { await task() }
                }
            }
        }
    }
    

We also can define a function as deprecated or obsoleted by using the
_@available_ attribute. In the example below, we define a function as
introduced in iOS 14, deprecated in iOS 15, and obsoleted in iOS 16. The
_introduced_ parameter defines the minimal platform version needed to run the
particular function.

    
    
    extension View {
        @available(iOS, introduced: 14, deprecated: 15, obsoleted: 16)
        @available(macOS, introduced: 11, deprecated: 12, obsoleted: 13)
        func backportedTask<Value: Equatable>(
            id: Value,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            if #available(iOS 15, macOS 12, *) {
                return self.task(id: id, task)
            } else {
                return self.onChange(of: id) { _ in
                    Task { await task() }
                }
            }
        }
    }
    

Swift compiler generates the warning whenever you build the project with iOS
15 as the target. When you try to build the project with the target version
iOS 16, it will generate a compiler error. This is the main difference between
deprecated and obsoleted parameters.

    
    
    extension View {
        @available(iOS, introduced: 14, deprecated: 16, obsoleted: 17, message: "Use `task` view modifier instead.")
        func backportedTask<Value: Equatable>(
            id: Value,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            if #available(iOS 15, macOS 12, *) {
                return self.task(id: id, task)
            } else {
                return self.onChange(of: id) { _ in
                    Task { await task() }
                }
            }
        }
    }
    

You can also use the _message_ parameter to allow Swift compiler provide an
error or warning message during compilation.

    
    
    extension View {
        @available(iOS, introduced: 14, deprecated: 16, obsoleted: 17, renamed: "task")
        func backportedTask<Value: Equatable>(
            id: Value,
            task: @Sendable @escaping () async -> Void
        ) -> some View {
            if #available(iOS 15, macOS 12, *) {
                return self.task(id: id, task)
            } else {
                return self.onChange(of: id) { _ in
                    Task { await task() }
                }
            }
        }
    }
    

Another variant of the _@available_ attribute allows us to mark the function
or type as renamed. In this case, Xcode allows the user to press the warning
message and shows the fix button that replaces the old name with the new one.

Swift 5.8 introduced the _@backDeployed_ attribute allowing you to back-deploy
the functionality introduced in new versions but relying on the old code.

    
    
    extension View {
        @available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
        @backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0)
        func task<Value: Equatable>(
            id: Value,
            closure: @Sendable @escaping () async -> Void
        ) -> some View {
            return self.onChange(of: id) { _ in
                Task { await closure() }
            }
        }
    }
    

Today we learned not only how to use the new APIs in the legacy codebase but
also how to be a good citizen on the platform and define the functions and
types with the platform availability information, which is crucial when you
work on a framework or library. I hope you enjoy the post. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and see you next week!

