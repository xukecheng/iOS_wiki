##  How to use GeometryReader without breaking SwiftUI layout

04 Nov 2020

Usually, I try to avoid _GeometryReader_ as much as I can. But sometimes, we
need it to build our custom view. This week we will talk about
_GeometryReader_ . The view that allows us to read its geometry and layout
child views manually.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Let’s start with a quick example of _GeometryReader_ usage.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            GeometryReader { geometry in
                Text("Hello!")
                    .frame(
                        width: geometry.size.width,
                        height: geometry.size.height
                    ).background(Color.red)
            }
        }
    }
    

Here we have a _GeometryReader_ in the root of our _ContentView_ . By default,
_GeometryReader_ places its children in the top left corner, which is very
unusual for SwiftUI views. Usually, SwiftUI views place content in the center
of its coordinate space.

As you can see, _GeometryReader_ ’s @ _ViewBuilder_ closure has the parameter
called geometry. This parameter is an instance of _GeometryProxy_ struct. You
can use an instance of _GeometryProxy_ to access information about the
coordinate space using the following properties.

  1. _size_ \- The size of space available to _GeometryReader_ . 
  2. _safeAreaInsets_ \- An instance of _EdgeInsets_ struct that provides safe area insets of _GeometryReader_ . 

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            GeometryReader { geometry in
                Text("Hello!")
                    .frame(
                        width: geometry.frame(in: .global).width,
                        height: geometry.frame(in: .global).height
                    ).background(Color.red)
            }
        }
    }
    

_GeometryProxy_ also has a _frame_ function that allows you to access the
frame of the _GeometryReader_ by converting it into a correct coordinate
space. You can also create your own coordinate spaces by using
_coordinateSpace_ modifier on any view.

> Take a look at [ “Building Bottom sheet in SwiftUI” ](/2019/12/11/building-
> bottom-sheet-in-swiftui/) post to learn more about advanced usages of
> _GeometryReader_ .

####  Hints to follow while using GeometryReader

Now we know how to use _GeometryReader_ and its benefits. It is a perfect time
to talk about its disadvantages. _GeometryReader_ fills all the available
space, and usually, it is not something you want to achieve.

If you use _GeometryReader_ as a full-screen view, that is great, and you
don’t need to do anything. In other cases, try to limit the available space of
_GeometryReader_ by using _frame_ or _aspectRatio_ modifiers. These modifiers
allow you to keep _GeometryReader_ under control.

The second tip is to use _GeometryReader_ inside an overlay or background of
any view. SwiftUI keeps overlay and background views in the same size as the
view that you apply them. It limits the size of _GeometryReader_ and doesn’t
allow it to grow and fill all the available space.

> To learn more about this approach, take a look at [ “The magic of view
> preferences in SwiftUI” ](/2020/01/15/the-magic-of-view-preferences-in-
> swiftui/) post.

In case when you need to draw something, you can replace the _GeometryReader_
by using Shape API. Shape API provides you all the needed information about
available space using _Path_ struct.

> To learn more about Shape API, look at [ “Building BarChart with Shape API
> in SwiftUI” ](/2019/08/14/building-barchart-with-shape-api-in-swiftui/)
> post.

####  Conclusion

I suggest you avoid _GeometryReader_ where you can. In the case where you sure
that you need it, try to follow my tips. These tips should save many hours of
debugging the SwiftUI layout. I hope you enjoy the post. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this article. Thanks for reading, and see you next week!

