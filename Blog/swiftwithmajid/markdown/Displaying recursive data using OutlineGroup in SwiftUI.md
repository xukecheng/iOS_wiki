##  Displaying recursive data using OutlineGroup in SwiftUI

02 Sep 2020

This week we will talk about another excellent UI component called
_OutlineGroup_ . Apple released _OutlineGroup_ during the WWDC20 side-by-side
with other great things, including grids, menus, and toolbars. I already
covered them in my previous posts. And finally, today is time to talk about
_OutlineGroup_ and _DisclosureGroup_ that handles the expanding behavior.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  OutlineGroup

_OutlineGroup_ is a view that enumerates tree-structured collection and
renders its view representation recursively. It is a perfect solution to
display recursive data like trees. Assume that you are working on the shopping
app where you obtain a categories tree via API. Let’s take a look at a
straightforward tree implementation in Swift.

    
    
    struct Tree<Value: Hashable>: Hashable {
        let value: Value
        var children: [Tree]? = nil
    }
    

Now we have a pretty simple tree structure that allows us to define complex
category hierarchy. For example, the API response from the categories endpoint
might look like this.

    
    
    let categories: [Tree<String>] = [
        .init(
            value: "Clothing",
            children: [
                .init(value: "Hoodies"),
                .init(value: "Jackets"),
                .init(value: "Joggers"),
                .init(value: "Jumpers"),
                .init(
                    value: "Jeans",
                    children: [
                        .init(value: "Regular"),
                        .init(value: "Slim")
                    ]
                ),
            ]
        ),
        .init(
            value: "Shoes",
            children: [
                .init(value: "Boots"),
                .init(value: "Sliders"),
                .init(value: "Sandals"),
                .init(value: "Trainers"),
            ]
        )
    ]
    

As you can see, we already have a recursive structure. Let’s try to feed it
into the _OutlineGroup_ to display the tree hierarchy.

    
    
    struct ContentView: View {
        var body: some View {
            OutlineGroup(categories, id: \.value, children: \.children) { tree in
                Text(tree.value).font(.subheadline)
            }
        }
    }
    

_OutlineGroup_ allows us to display very complex tree-structured collections
in a few lines of code. We construct _OutlineGroup_ in a very familiar
fashion. It looks similar to the _ForEach_ view but also needs the children
parameter. Children parameter is a _KeyPath_ to a recursive property of our
structure. Keep in mind that the recursive property must be optional. This is
how _OutlineGroup_ understands the end of the tree node.

![outline group](/public/outlineGroup1.png)

Another thing that Apple released side-by-side with _OutlineGroup_ is a new
way to configure a _List_ that uses _OutlineGroup_ to display its items. It
automatically applies list styling to _OutlineGroup_ and allows us to use it
in the sidebar navigation. Let’s take a look at how we can use List with
_OutlineGroup_ under the hood.

    
    
    struct ContentView: View {
        var body: some View {
            List(categories, id: \.value, children: \.children) { tree in
                Text(tree.value).font(.subheadline)
            }.listStyle(SidebarListStyle())
        }
    }
    

As you can see, there is a new _List_ initializer that takes additional
children parameter. You can simply replace your _OutlineGroup_ with _List_ ,
and you will get a list styling for your tree-structured collection.

![outline group](/public/outlineGroup2.png)

> To learn more about building three-column navigation in SwiftUI, take a look
> at my [ “Sidebar navigation in SwiftUI” ](/2020/07/21/sidebar-navigation-in-
> swiftui/) post.

_OutlineGroup_ is really shining when you use it inside a _List_ . We can use
_OutlineGroup_ inside sections. This approach allows us to expand the first
level of your tree-structured collection automatically. It looks gorgeous with
sidebar style. Let’s take a look at the quick example of section-based
_OutlineGroup_ usage.

    
    
    struct ContentView: View {
        var body: some View {
            List {
                ForEach(categories, id: \.self) { section in
                    Section(header: Text(section.value)) {
                        OutlineGroup(
                            section.children ?? [],
                            id: \.value,
                            children: \.children
                        ) { tree in
                            Text(tree.value)
                                .font(.subheadline)
                        }
                    }
                }
            }.listStyle(SidebarListStyle())
        }
    }
    

![outline group](/public/outlineGroup3.png)

####  DisclosureGroup

As you can see on the screenshots that I provide during the post, the main
component of _OutlineGroup_ is an expandable view called _DisclosureGroup_ .
_DisclosureGroup_ is a straightforward view that accepts title string, content
view, and boolean binding, which shows or hides the content.

    
    
    struct ContentView: View {
        @State private var showContent = false
    
        var body: some View {
            DisclosureGroup("Message", isExpanded: $showContent) {
                Text("Hello World!")
            }
        }
    }
    

You can use _DisclosureGroup_ inside a _Form_ view that allows you to build
complex forms quickly in a very declarative way.

> To learn more about the power of Form view in SwiftUI, take a look at my [
> “Building forms with SwiftUI” ](/2019/06/19/building-forms-with-swiftui/)
> post.

####  Conclusion

Today we learned about another view that WWDC20 brings us in addition to the
current collection of views. With the help of _OutlineGroup_ , we can easily
display the massive collection of tree-structured items.

We also learned about _DisclosureGroup_ that powers _OutlineGroup_ . The nice
bonus is that we can use _DisclosureGroup_ separately. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this article. Thanks for reading, and see you next
week!

