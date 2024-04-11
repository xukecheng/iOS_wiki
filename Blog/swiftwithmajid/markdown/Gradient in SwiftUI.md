##  Gradient in SwiftUI

13 Nov 2019

One thing which I really enjoy about SwiftUI is the fact that SwiftUI has a
lot of stuff ready to use out of the box. In order to build your app, all you
need to do is composing the building blocks provided by SwiftUI into a fully
functional application. This week we will talk about _Gradient_ , which is
just another type of _View_ in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

As I already said, _Gradient_ is one of the _View_ protocol’s implementations.
You can easily use _Gradient_ anywhere in the app where you can use other
_View_ components like _Text_ or _Button_ . SwiftUI provides three types of
_Gradient_ component. Let’s take a look at them one by one.

####  LinearGradient

_LinearGradient_ is one of the basic types of _Gradient_ . It draws colors
from the start point to the end point. I think the best way to understand
gradients is just writing the code and check the results. Let’s try it.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            LinearGradient(
                gradient: Gradient(colors: [.red, .white]),
                startPoint: .top,
                endPoint: .bottom
            )
        }
    }
    

![example1](/public/l1.png)

As you can see, _LinearGradient_ applies red to white transition from top to
bottom as we pointed it in the code. Start and end points are the cases of
_UnitPoint_ enum. These points can take the following values: _.zero, .center,
leading, trailing, top, bottom, topLeading, topTrailing, bottomLeading,
bottomTrailing_ . SwiftUI uses these unit point values to convert the
declarative description into real coordinates of the view. Let’s check another
unit point values.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            LinearGradient(
                gradient: Gradient(colors: [.red, .white]),
                startPoint: .leading,
                endPoint: .trailing
            )
        }
    }
    

I’ve changed the start and end points to leading and trailing. It will help us
to understand the meaning of unit points better, and here is the result.

![example2](/public/l2.png)

_LinearGradient_ is a commonly used gradient type. You can use it as a
background for a _Text_ component, which you might want to draw ahead of an
_Image_ .

####  RadialGradient

_RadialGradient_ applies color transformation from the defined center point to
its circle edge, which is calculated using the start and end radius. Let’s
take a look at a quick example of _RadialGradient_ .

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            RadialGradient(
                gradient: Gradient(colors: [.orange, .white]),
                center: .center,
                startRadius: 1,
                endRadius: 200
            )
        }
    }
    

![example3](/public/r1.png)

I suggest you play around the _RadialGradient_ with more colors and different
center positions to understand it even better.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            RadialGradient(
                gradient: Gradient(colors: [.orange, .white, .orange, .white]),
                center: .center,
                startRadius: 1,
                endRadius: 200
            )
        }
    }
    

![example4](/public/r2.png)

Sometimes we need to use _RadialGradient_ inside the _GeometryReader_ to
calculate proper radius value relative to the parent’s size. To learn more
about _GeometryReader_ , take a look at [ “Building BarChart with Shape API in
SwiftUI” ](/2019/08/14/building-barchart-with-shape-api-in-swiftui/) post.

####  AngularGradient

The last type of _Gradient_ which we have in SwiftUI is _AngularGradient_ .
I’m not using it very ofter, but it has a very nice color transformation
effect. _AngularGradient_ also is known as the conic _Gradient_ . This
_Gradient_ type applies color transformation as the angle changes, relative to
a center point. Let’s check out the code sample and resulting image.

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            AngularGradient(
                gradient: Gradient(colors: [.orange, .white]),
                center: .center
            )
        }
    }
    

![example5](/public/a1.png)

Let’s take a look at a different example by adding more colors to the
_Gradient_ .

    
    
    import SwiftUI
    
    struct ContentView: View {
        var body: some View {
            AngularGradient(
                gradient: Gradient(
                    colors: [
                        .orange, .white, .orange, .white, .orange, .white, .orange, .white, .orange
                    ]
                ),
                center: .center
            )
        }
    }
    

![example6](/public/a2.png)

By default, SwiftUI provides us _AngularGradient_ with start and end angles,
which equal to zero, but you can adjust them by using another overload of the
initializer.

####  Conclusion

This week we learned how to use _Gradients_ in SwiftUI. I usually use only
_LinearGradient_ to cover my images and then put some text on top of them, but
who knows which crazy designs your designer will bring you. I hope you enjoy
the post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and
ask your questions related to this post. Thanks for reading, and see you next
week!

