##  Customizing the shape of views in SwiftUI

12 Feb 2020

SwiftUI provides us several exciting ways to change the shape of our views. It
allows clipping, masking, and a few other operations on the shape of views.
This week I want to talk to you about altering view’s shape in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Clipping

Sometimes we use the frame modifier to limit the size of our view. It might be
useful when you want to set the size to the image that should be scaled. In
case when the scaled image bigger than the provided frame, it can exceed it
and overlap other views. To fix this issue, SwiftUI allows us to clip the
content of the view to its frame. Let’s take a look at a quick example.

    
    
    KFImage(recipe.image)
        .resizable()
        .aspectRatio(contentMode: .fill)
        .frame(height: 300)
        .clipped(antialiased: true)
    

As you can see in the example above, we use the _clipped_ modifier. This
modifier lets us cut the content of the view inside its bounds. It also takes
the argument that indicates whenever to apply smoothing to the edges of the
frame.

> _KFImage_ is a part of [ KingFisher ](https://github.com/onevcat/Kingfisher)
> library for loading remote images

####  Clipping the shape

Assume that you are working on the app that presents the avatars. Usually, our
designers want to make avatars in a rounded form. Fortunately, SwiftUI allows
us to clip the view into any shape we can imagine. SwiftUI provides an
exceptional modifier for that called _clipShape_ . Let’s take a look at how we
can use it.

    
    
    KFImage(user.avatar)
        .resizable()
        .aspectRatio(contentMode: .fill)
        .frame(width: 100, height: 100)
        .clipShape(Circle())
    

We can easily apply _clipShape_ to any view by providing the shape we want.
There are plenty of ready to use shapes like _Rectangle, Capsule, Circle, etc_
. provided by SwiftUI. But anytime you want something unique, for example, a
star form, you can quickly implement it by creating a struct conforming
_Shape_ protocol. You can apply any shape you want by doing your math in
_path_ function.

> To learn more about _Shape_ protocol, take a look at my [ “Building BarChart
> with Shape API in SwiftUI” post ](/2019/08/14/building-barchart-with-shape-
> api-in-swiftui/) .

###  Masking

Let’s take a look at more complex examples. Assume that you have a text
component that should use a gradient as the text color. You can’t implement it
by using the _foregroundColor_ modifier because it accepts only colors. It is
the exact case where we might use masking. Let’s take a look at how we can
apply masking to use a gradient as the text color.

    
    
    struct MaskSample: View {
        var body: some View {
            LinearGradient(
                gradient: Gradient(colors: [.blue, .green, .yellow, .orange, .red]),
                startPoint: .leading,
                endPoint: .trailing
            )
                .mask(Text("I love SwiftUI !!!").font(.largeTitle))
                .background(Color.black)
        }
    }
    

As you can see in the example above, we have a gradient that masked with the
text. SwiftUI allows us to cut our gradient into the shape of our text.
Remember that you can mask any view not only gradient. It means you can mask
any image with the text to provide a beautiful look and feel to your users.

![mask](/public/mask.png)

####  Conclusion

This week we learned about clipping and masking views in SwiftUI. Both
clipping and masking allow us to provide nice effects to our users by adding a
few lines of code. I hope you enjoy the post. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

