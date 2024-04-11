##  The power of @ViewBuilder in SwiftUI

18 Dec 2019

Last week we started a series of posts about developing interactive components
using SwiftUI, where we talked about building the bottom sheet. We need to
understand the power of _@ViewBuilder_ before moving to the next post about
building another interactive view. That’s why this week, we will talk about
_@ViewBuilder_ and its benefits while developing custom views.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Result builders

_@ViewBuilder_ is one of the possible result builders. The result builder
feature of Swift is described in [ Swift Evolution Proposal
](https://github.com/apple/swift-evolution/blob/main/proposals/0289-result-
builders.md) . The main goal of result builder is providing _DSL_ like syntax.
Let’s take a look at a very quick example of _@ViewBuilder_ usage.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            HStack{
                Text("hello")
                Text("world")
            }
        }
    }
    

We need to go down one layer to understand how _@ViewBuilder_ works.

    
    
    @inlinable public init(
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    )
    

Here is the declaration of _HStack_ view, as you can see the content closure
inside the init method marked with _@ViewBuilder_ . It means that expression
inside that closure needs to be handled by _@ViewBuilder_ . The swift compiler
will try to find the static buildBlock method declared in _@ViewBuilder_
struct that has two views as parameters. Let’s take a look at _@ViewBuilder_
struct declaration to find that method.

    
    
    @available(iOS 13.0, OSX 10.15, tvOS 13.0, watchOS 6.0, *)
    extension ViewBuilder {
        public static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> TupleView<(C0, C1)> where C0 : View, C1 : View
    }
    

As you can see, _@ViewBuilder_ has a static _buildBlock_ method that accepts
two views, combine them and return _TupleView_ . It also has other
declarations of _buildBlock_ method, which takes from one to ten child views,
and all of them combine child views into a _TupleView_ . That’s why
_@ViewBuilder_ can accept only ten views inside the closure.

    
    
    struct ContentView: View {
        @ObservedObject var viewModel: ViewModel
    
        @ViewBuilder
        var body: some View {
            if viewModel.isAuthorized {
                Text("Hello World!")
            } else {
                LoginView(viewModel: viewModel)
            }
        }
    }
    

_@ViewBuilder_ also has support for conditions via _if_ and _switch_
expressions.

    
    
    struct ContentView: View {
        @ObservedObject var viewModel: ViewModel
    
        @ViewBuilder
        var body: some View {
            switch viewModel.isAuthorized {
            case true:
                Text("Hello")
            case false:
                LoginView(viewModel: viewModel)
            }
        }
    }
    

> To learn how to avoid ten views limitation, take a look at my [ “View
> Composition in SwiftUI” ](/2019/10/30/view-composition-in-swiftui/) post.

####  TupleView

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            HStack{
                Text("hello")
                Text("world")
            }
        }
    }
    
    print(Mirror(reflecting: ContentView().body))
    // Mirror for HStack<TupleView<(Text, Text)>>
    

_TupleView_ is a view created from a swift tuple of view values. _TupleView_
doesn’t have any logic inside. It just holds the views. _TupleView_ completely
transparent and behaves like its parent view. It means when you put it inside
the _HStack_ , _TupleView_ places the views from the tuple in a horizontal
direction.

####  Using @ViewBuilder

Now we know all the needed things to build our own custom view container,
which uses _@ViewBuilder_ . Assume that our app needs a notification view. The
notification view should have a consistent design and appear in the top of the
screen, but content can be various. It is a perfect use case for
_@ViewBuilder_ . Let’s see how we can utilize it.

    
    
    import SwiftUI
    
    struct NotificationView<Content: View>: View {
        let content: Content
    
        init(@ViewBuilder content: () -> Content) {
            self.content = content()
        }
    
        var body: some View {
            content
                .padding()
                .background(Color(.tertiarySystemBackground))
                .cornerRadius(16)
                .transition(.move(edge: .top))
                .animation(.spring())
        }
    }
    

As you can see, we use _@ViewBuilder_ to mark our content closure. It gives us
the opportunity to use _NotificationView_ in the same way as _VStack_ or
_HStack_ . Here is the example of using _NotificationView_ .

    
    
    import SwiftUI
    
    struct ContentView: View {
        @State private var notificationShown = false
    
        var body: some View {
            VStack {
                if self.notificationShown {
                    NotificationView {
                        Text("notification")
                    }
                }
    
                Spacer()
    
                Button("toggle") {
                    self.notificationShown.toggle()
                }
    
                Spacer()
            }
        }
    }
    

> We also used the ability to build custom views via _@ViewBuilder_ during [
> “Building Bottom sheet in SwiftUI” ](/2019/12/11/building-bottom-sheet-in-
> swiftui/) post.

####  Conclusion

This week we talked about the benefits of result builders and used
_@ViewBuilder_ as a concrete example. _@ViewBuilder_ allows us to build super
reusable SwiftUI views by separating its presentation logic and content. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

