##  Alignment guides in SwiftUI

11 Mar 2020

This week we will talk about another great tool that we have in SwiftUI. The
alignment guide is a way that we can use to speak to SwiftUI’s layout system.
By using alignment guides, we can easily align views that live in different
parts of a view hierarchy.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

SwiftUI provides us a few container views that we can use to build our layout.
You might already be familiar with _VStack, HStack, and ZStack_ . All of these
container views use alignments to regulate the position of child views inside
the container. Let’s take a look at the very basic example.

    
    
    VStack(alignment: .leading) {
        Text("Toronto")
        Text("Paris")
        Text("London")
        Text("Madrid")
    }
    

In the example above, we have a vertical container view that displays child
views from the top to bottom. We set alignment to leading, and it means that
_VStack_ will use the leading point of every child view to align them.

_VStack_ uses _HorizontalAlignment_ enum to define possible alignments. On the
other hand, _HStack_ uses _VerticalAlignment_ enum. It might be strange, but
after all, it is logical. We can set the alignment of _VStack_ only in the
horizontal way because the container view controls the vertical direction.
_ZStack_ uses _Alignment_ enum, which is the combination of
_HorizontalAlignment_ and _VerticalAlignment_ enums.

####  Overriding alignment guides

SwiftUI allows us to override standard alignments by using the
_alignmentGuide_ modifier. For example, we might need to align the bottom of
_Image_ and _Text_ views in a horizontal stack. We can face the problem when
image has some spacing inside a bitmap, and it looks not aligned very well.
This is a perfect case for overriding an alignment guide.

    
    
    struct ContentView: View {
        var body: some View {
            HStack(alignment: .bottom) {
                Image(systemName: "zzz")
                    .alignmentGuide(.bottom) { d in d[.bottom] + 8 }
                Text("Sleep")
            }
        }
    }
    

As you can see in the example above, we use _alignmentGuide_ modifier to
override the default value for . _bottom_ alignment by adding 8 points. We
read the default value by using subscript of **d** , which is an instance of
_ViewDimensions_ struct. _ViewDimensions_ struct provides us access to the
width and height of the view and default alignment values by using a
subscript.

####  Custom alignment guides

We learned how to override default alignments in SwiftUI, but SwiftUI also
allows us to create a custom alignment guide that we can use in container
views to align its child views. But why we might need it? Custom alignments
allow us to align views that live in different container views. Let’s take a
look at the example below.

    
    
    struct ContentView: View {
        var body: some View {
            HStack(alignment: .center) {
                Image(systemName: "star")
                VStack(alignment: .center) {
                    Text("Toronto")
                    Text("Paris")
                    Text("London")
                    Text("Madrid")
                }
            }
        }
    }
    

We have a horizontal stack that contains an image and vertical stack with a
few text views. I might need to align the image with the third text view, but
it doesn’t look possible with the current configuration, because these views
live in different containers. Fortunately, SwiftUI allows us to create a
custom alignment and use it in the parent container view.

    
    
    extension VerticalAlignment {
        struct CustomAlignment: AlignmentID {
            static func defaultValue(in context: ViewDimensions) -> CGFloat {
                return context[VerticalAlignment.center]
            }
        }
    
        static let custom = VerticalAlignment(CustomAlignment.self)
    }
    
    struct ContentView: View {
        var body: some View {
            HStack(alignment: .custom) {
                Image(systemName: "star")
                VStack(alignment: .leading) {
                    Text("Toronto")
                    Text("Paris")
                    Text("London")
                        .alignmentGuide(.custom) { $0[VerticalAlignment.center] }
                    Text("Madrid")
                }
            }
        }
    }
    

In the example above, we use _AlignmentID_ protocol to create a custom
alignment. This protocol has the only requirement that we need to provide.
SwiftUI will use the _defaultValue_ whenever we leave it without custom value.
The interesting fact is that the inner _VStack_ didn’t specify a value for
custom alignment, but it uses the value that provides its child view.

![align](/public/align.png)

####  Conclusion

Today we learned how powerful could be custom alignments in SwiftUI. We also
can use the overriding alignment technique to build super custom layouts. For
example, we can build a grid view that arranges child views using alignments.
I suggest you play around alignments to understand it well. It is something
that can take time. I hope you enjoy the post. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

