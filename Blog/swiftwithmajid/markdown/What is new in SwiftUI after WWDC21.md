##  What is new in SwiftUI after WWDC21

08 Jun 2021

WWDC21 is finally here, and there are many new things in the updated version
of SwiftUI. I’m happy to share with you that many items on my wishlist have
finally arrived. In this post, I will try to give you a summary of the
significant SwiftUI additions of this year.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  List

The _List_ view is the most common view in our apps. The _List_ view managed
_UITableView_ under the hood but didn’t expose all the great features of
_UITableView_ till today. Now we have view modifiers that expose the styling
options for separators and tint colors in sections and cells. Let’s see how we
can use them.

    
    
    struct ContentView: View {
        @State private var messages: [String] = [
            "Hello", "World"
        ]
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(messages, id: \.self) { message in
                        Text(message)
                            .listRowSeparatorTint(Color.red)
                            .listRowSeparator(.visible, edges: .all)
                    }
                }
                .listSectionSeparator(.visible, edges: .all)
                .listSectionSeparatorTint(Color.purple)
                .navigationTitle("Messages")
            }
        }
    }
    

SwiftUI also provides the new _swipeActions_ view modifier that we can use to
attach the swipeable action to views inside a list.

    
    
    struct ContentView: View {
        @State private var messages: [String] = [
            "Hello", "World"
        ]
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(messages, id: \.self) { message in
                        Text(message)
                            .swipeActions(edge: .trailing, allowsFullSwipe: false) {
                                Button("Remove", role: .destructive) {
                                    messages.removeAll { $0 == message }
                                }
                            }
                            .swipeActions(edge: .leading, allowsFullSwipe: true) {
                                Button("Copy") {
                                    messages.append(message)
                                }
                            }
                    }
                }.navigationTitle("Messages")
            }
        }
    }
    

As you can see in the example above, we also have new _ButtonRole_ enum that
allows specifying a role for the button, which can be either _destructive_ or
_cancel_ .

####  Pull-to-Refresh

I used to have the pull-to-refresh gesture in the screens where the content
can be updated or refetched. SwiftUI provides the new _refreshable_ view
modifier that we can use to attach the pull-to-refresh gesture and a callback
that SwiftUI runs as soon as the user enables the gesture.

    
    
    struct ContentView: View {
        @State private var messages: [String] = [
            "Hello", "World"
        ]
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(messages, id: \.self) { message in
                        Text(message)
                    }
                }.refreshable {
                    messages.append("!!!")
                }
                .navigationTitle("Messages")
            }
        }
    }
    

####  Search

Another thing that I really missed in SwiftUI is _SearchBar_ and
_SearchController_ ’s functionality. Fortunately, this iteration of SwiftUI is
packed with a brand new collection of view modifiers that enables powerful
search capabilities.

    
    
    struct ContentView: View {
        @State private var query: String = ""
        @State private var messages: [String] = [
            "Hello", "World"
        ]
    
        var body: some View {
            NavigationView {
                List {
                    ForEach(messages, id: \.self) { message in
                        Text(message)
                    }
                }
                .searchable("Search term", text: $query, placement: .automatic)
                .onChange(of: query) { print($0) }
                .navigationTitle("Messages")
            }
        }
    }
    

####  AsyncImage

The thing I didn’t expect was the new _AsyncImage_ view. _AsyncImage_ view
allows you to download and present remote images using _URLSession_ . It
provides a very lovely API which very easy to use. Let’s take a look at it.

    
    
    struct Post: Hashable {
        let image: URL
        let title: String
        let content: String
    }
    
    struct PostView: View {
        let post: Post
    
        var body: some View {
            HStack {
                AsyncImage(url: post.image)
                VStack {
                    Text(post.title)
                    Text(post.content)
                        .foregroundColor(.secondary)
                }
            }
        }
    }
    

####  Text and AttributedString

Swift Foundation has a new _AttributedString_ type and SwiftUI supports it out
of the box. You can now pass the instances of _AttributedString_ to _Text_
view to display it. An interesting detail here is the ability to display
markdown content using the new _AttributedString_ .

    
    
    struct PostView: View {
        let post: Post
    
        var markdown: AttributedString {
            try! AttributedString(markdown: post.content)
        }
    
        var body: some View {
            HStack {
                AsyncImage(url: post.image)
                VStack {
                    Text(post.title)
                    Text(markdown)
                }
            }
        }
    }
    

As the bonus we gain markdown support everywhere with _Text_ view.

    
    
    struct ContentView: View {
        var body: some View {
            Text("**Happy WWDC21**")
        }
    }
    

####  Focus management

Finally, SwiftUI provides us a way to manage the focus in our views. There are
brand new @ _FocusState_ property wrappers and a _focused_ view modifier that
we can use to toggle first responders.

    
    
    struct LoginForm: View {
        enum Field: Hashable {
            case usernameField
            case passwordField
        }
    
        @State private var username = ""
        @State private var password = ""
        @FocusState private var focusedField: Field?
    
        var body: some View {
            VStack {
                TextField("Username", text: $username)
                    .focused($focusedField, equals: .usernameField)
    
                SecureField("Password", text: $password)
                    .focused($focusedField, equals: .passwordField)
    
                Button("Sign In") {
                    if username.isEmpty {
                        focusedField = .usernameField
                    } else if password.isEmpty {
                        focusedField = .passwordField
                    } else {
                        handleLogin(username, password)
                    }
                }
            }
        }
    }
    

####  Canvas

SwiftUI _Canvas_ is a new way to gain more control over lower-level drawing
primitives. It is a modern, GPU-accelerated equivalent of _drawRect_ . We can
use _Canvas_ to draw shapes using _Path_ . We can also draw images, texts, and
other SwiftUI views.

    
    
    struct ContentView: View {
        var body: some View {
            Canvas { context, size in
                context.fill(
                    Circle().path(in: .init(origin: .zero, size: size)),
                    with: .color(.green)
                )
            }
        }
    }
    

####  Materials

iOS provides materials or blur effects that create a translucent effect you
can use to evoke a sense of depth. The effect of material lets views and
controls hint at background content without distracting from foreground
content. We didn’t have access to materials in previous versions of SwiftUI.
Fortunately, the new version of SwiftUI provides us a whole range of physical
materials from ultra-thin to ultra-thick and semantic bars material.

    
    
    ZStack {
        Color.teal
        Label("Flag", systemImage: "flag.fill")
            .padding()
            .background(.regularMaterial)
    }
    

####  TimelineView

_TimelineView_ is another brand new SwiftUI view. Usually, SwiftUI updates
views only during environment or state changes. In case of _TimelineView_ ,
SwiftUI updates it according to a schedule that you provide. It might be very
useful while building clock or workout apps.

    
    
    TimelineView(PeriodicTimelineSchedule(from: startDate, by: 1)) { context in
        AnalogTimerView(date: context.date)
    }
    

####  Conclusion

There are many other additions worth mentioning, like a brand new
Accessibility Rotors API, the new _SectionedFetchRequest_ property wrapper
that allows you to make sectioned requests to Core Data, and much more.

I hope to cover all these new features of the SwiftUI framework in the
upcoming weeks. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

