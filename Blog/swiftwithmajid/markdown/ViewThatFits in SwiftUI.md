##  ViewThatFits in SwiftUI

26 Jul 2022

How often did you use _GeometryReader_ to measure layout and place different
views? _GeometryReader_ was always a great tool in our toolbox, but It is
elementary to break the layout while using the _GeometryReader_ . Fortunately,
the next generation of the SwiftUI framework introduces a new way to measure
available space and place different views. This week we will learn how to use
the brand new _ViewThatFits_ view.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The introduced _ViewThatFits_ view is elementary to use. You don’t need to
manually measure available space or calculate if the particular view fits into
the available space. All you need to do is to create an instance of the
_ViewThatFits_ view and place in its _ViewBuilder_ closure up to 10 views.
_ViewThatFits_ automatically measures available space and the size of its
children and takes the first view that perfectly fits the available space.
That’s it.

    
    
    struct ContentView: View {
        var body: some View {
            ViewThatFits {
                HugeView()
                MediumView()
                SmallView()
            }
        }
    }
    

As you can see in the example above, it is straightforward to use the new
_ViewThatFits_ view. But you should be careful about the order of the passed
views. _ViewThatFits_ uses the first view that fits the available space. It
means that you should usually place your views from the biggest to the
smallest.

> To learn how to use the GeometryReader properly, look at my [ “How to use
> GeometryReader without breaking SwiftUI layout” ](/2020/11/04/how-to-use-
> geometryreader-without-breaking-swiftui-layout/) post.

By default, the _ViewThatFits_ view considers all the available space, but you
can set the particular axis you need to measure. For example, it might be a
horizontal or vertical axis.

    
    
    struct ContentView: View {
        var body: some View {
            ViewThatFits(in: .horizontal) {
                HugeView()
                MediumView()
                SmallView()
            }
        }
    }
    

In the current example, we completely ignore the vertical axis and consider
only horizontally available space. Let me describe the steps the
_ViewThatFits_ view applies while choosing a view.

  1. _ViewThatFits_ measures available space for a particular axis or both of them. 
  2. It measures the size of the first view and places it if it fits the available space. 
  3. It measures the size of the second view if the first one doesn’t fit the available space and place the second one if it fits. 
  4. It places the last view in the _ViewBuilder_ closure if no view fits the available space. 

Today we learned the new and easy way of measuring available space and placing
a view fitting that space. I hope you enjoy the post. Feel free to follow me
on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and see you next week!

