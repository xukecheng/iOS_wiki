##  Layout priorities in SwiftUI

15 Apr 2020

This week we will talk about another core process in SwiftUI. We will learn
the procedure of laying out views. We will understand how SwiftUI calculates
positions and sizes of our views and how we can change that process using
layout priorities.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

You can build regular views without real knowledge of the layout process.
SwiftUI has a declarative nature where you have to describe what you want to
achieve, and SwiftUI will understand it. Let’s start our discussion with the
simple example of a “Hello World” app in SwiftUI.

    
    
    import SwiftUI
    
    struct MessageView: View {
        var body: some View {
            Text("Hello World!!!")
        }
    }
    

Assume that _MessageView_ is the root view of our app.

  1. SwiftUI passes all the available space to _MessageView_ . 
  2. _MessageView_ has only one child, which is the text view. _MessageView_ proposes the available space to the text view and asks it to calculate its size. 
  3. The text view measures the size of its content and passes it back to _MessageView_ . 
  4. _MessageView_ now understands the size of the text view and place it in the center of available space. 

This is how the SwiftUI layout system works. It always applies these four
steps.

####  Layout Priority

Let’s take a look at the more complicated example with multiple sibling views
inside an _HStack_ .

    
    
    import SwiftUI
    
    struct MessageView: View {
        var body: some View {
            HStack(spacing: 16) {
                Text("Hello")
                Text("World")
                Text("!!!")
            }
            .font(.largeTitle)
        }
    }
    

Vertical and horizontal stacks have additional steps in the layout process.

  1. First of all, stack view calculates adaptive spacing between items and deducts it from available space. 
  2. Then stack view divides available space into equal parts and offers one of them to the first child. 
  3. The child view calculates its size and returns it to the parent stack. 
  4. As the next step, stack deducts the size of the first child from available space and divide it into equal portions again. 
  5. Stack view repeats this process as many times as needed to calculate the size of every child. 
  6. It the end, stack view sum the spacing between items and calculated sizes of children to understand its own size and pass it back to the parent. 

One thing that we can adjust in this process is the order of size proposing.
Usually, SwiftUI starts the layout process inside a stack with the least
flexible view. But we can alter this rule by using _layoutPriority_ modifier.

Layout priority defines the order of the size proposing process. By default,
all views have 0 as default priority. SwiftUI allows us to set a custom layout
priority using _layoutPriority_ modifier. SwiftUI uses layout priorities to
sort views in descending order. It means SwiftUI will propose views with
higher priority first.

    
    
    import SwiftUI
    
    struct MessageView: View {
        var body: some View {
            HStack(spacing: 16) {
                Text("Hello")
                Text("World")
                Text("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    .layoutPriority(1)
            }
            .font(.largeTitle)
            .lineLimit(1)
        }
    }
    

As you can see in the example above, we use _layoutPriority_ modifier to
change the order of the layout process. SwiftUI will start the size proposing
process with the latest view inside the _HStack_ because it has the highest
priority in the view hierarchy. Try to remove _layoutPriority_ modifier to
understand how it works.

####  Conclusion

This week we learned about another exciting feature of SwiftUI. To be honest,
I don’t use layout priorities a lot. Usually, I’m able to build the needed
layout without altering priorities, but it is always good to know that we have
this tool in the toolbox. I hope you enjoy the post. Feel free to follow me on
[ Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

