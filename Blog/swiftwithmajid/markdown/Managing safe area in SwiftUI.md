##  Managing safe area in SwiftUI

03 Nov 2021

A safe area defines the area within a view that isn’t covered by a navigation
bar, tab bar, toolbar, or other views. SwiftUI views respect safe areas out of
the box. But there are plenty of situations when you need to customize this
behavior. This week we will learn how to manage the safe area in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Safe areas help us to keep our views inside the visible parts of the screen.
For example, we can easily place our views between the navigation bar and home
indicator using a safe area.

![safe-area](/public/safearea10.png)

By default, SwiftUI place views only inside the safe area. Here is the example
showing that.

    
    
    struct ContentView: View {
        var body: some View {
            NavigationView {
                ZStack {
                    LinearGradient(
                        colors: [.red, .yellow],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                    .navigationTitle("Hello World")
                }
            }
        }
    }
    

![safe-area](/public/safearea1.png)

But we can change this behavior using the _ignoresSafeArea_ view modifier.

    
    
    struct ContentView: View {
        var body: some View {
            NavigationView {
                ZStack {
                    LinearGradient(
                        colors: [.red, .yellow],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                    .ignoresSafeArea()
                    .navigationTitle("Hello World")
                }
            }
        }
    }
    

![safe-area](/public/safearea2.png)

The _ignoresSafeArea_ view modifier expands the view and fills the space by
ignoring the safe area. The _ignoresSafeArea_ view modifier has two parameters
that allow us to set the direction and the region of the ignored safe area.

    
    
    struct ContentView: View {
        var body: some View {
            NavigationView {
                ZStack {
                    LinearGradient(
                        colors: [.red, .yellow],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                    .ignoresSafeArea(.keyboard, edges: .bottom)
                    .ignoresSafeArea(.container, edges: [.top, .horizontal])
                    .navigationTitle("Hello World")
                }
            }
        }
    }
    

Let’s take a deep look at the possible parameters of the _ignoresSafeArea_
view modifier.

  1. The _regions_ parameter allows us to set the ignored safe area type. For example, it might be a parent container, keyboard, or all of them. 
  2. The _edges_ parameter allows us to ignore the safe area in the following direction or set of directions. For example, it could be _top, leading, bottom, trailing, horizontal, vertical, all_ , or any combination of previous options. 

####  safeAreaInset view modifier

The _safeAreaInset_ view modifier is another way to manage the safe area of
the view. The _safeAreaInset_ view modifier allows you to shift the safe area
of the view by placing another view inside the original safe area of the view.

    
    
    struct ContentView: View {
        var body: some View {
            NavigationView {
                LinearGradient(
                    colors: [.red, .yellow],
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                .ignoresSafeArea()
                .navigationTitle("Hello World")
                .safeAreaInset(edge: .bottom, alignment: .center, spacing: 0) {
                    Color.clear
                        .frame(height: 20)
                        .background(Material.bar)
                }
            }
        }
    }
    

![safe-area](/public/safearea3.png)

As you can see in the example above, the _safeAreaInset_ view modifier has a
bunch of parameters that allow us to control the spacing, alignment, and edge
of the shifted safe area. It also uses the _@ViewBuilder_ closure to build the
content of view that SwiftUI places in the space of the shifted safe area.

  1. _edge_ parameter allows you to set the vertical or horizontal edge of the shifted safe area region. 
  2. _spacing_ parameter allows you to put some space between the shifted safe area and the view itself. 
  3. _alignment_ parameter applies the horizontal or vertical alignment. 
  4. _content_ is the _@ViewBuilder_ closure that defines the content of the shifted safe area. 

> To learn more about materials in SwiftUI, take a look at my dedicated [
> “Blur effect and materials in SwiftUI” ](/2021/10/28/blur-effect-and-
> materials-in-swiftui/) post.

####  Conclusion

Today we learned how to manage the safe area in SwiftUI. Usually, we don’t
need it because SwiftUI handles it automatically. But feel free to customize
the look and feel of your content with an immersive experience using safe area
view modifiers. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

