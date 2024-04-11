##  Custom accessibility content in SwiftUI

06 Oct 2021

SwiftUI Release 3 brought a lot of new accessibility APIs, which we can use to
improve user experience drastically in an effortless way. This week I want to
talk about another new API that allows us to provide customized accessibility
content using the new _accessibilityCustomContent_ view modifier in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Let’s start with a simple example that defines the _User_ struct and a view
presenting an instance of the _User_ struct.

    
    
    import SwiftUI
    
    struct User: Decodable {
        let name: String
        let email: String
        let address: String
        let age: Int
    }
    
    struct UserView: View {
        let user: User
    
        var body: some View {
            VStack(alignment: .leading) {
                Text(user.name)
                    .font(.headline)
                Text(user.address)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                Text(user.email)
                    .foregroundColor(.secondary)
                Text("Age: \(user.age)")
                    .foregroundColor(.secondary)
            }
        }
    }
    

SwiftUI provides us with excellent accessibility support out of the box. You
don’t need to do anything to make your _UserView_ accessible. Every piece of
text inside the _UserView_ is accessible for assistive technologies like
VoiceOver and Switch Control. It might sound good, but it can overwhelm
VoiceOver users with a lot of data. Let’s improve accessibility support a
little bit but adding a few accessibility modifiers to our _UserView_ .

    
    
    struct UserView: View {
        let user: User
    
        var body: some View {
            VStack(alignment: .leading) {
                Text(user.name)
                    .font(.headline)
                Text(user.address)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                Text(user.email)
                    .foregroundColor(.secondary)
                Text("Age: \(user.age)")
                    .foregroundColor(.secondary)
            }
            .accessibilityElement(children: .ignore)
            .accessibilityLabel(user.name)
        }
    }
    

As you can see in the example above, we use accessibility modifiers to ignore
the accessibility content of the children to make the stack itself an
accessibility element. We also add the accessibility label to the stack but
still miss the other parts. We want to make all the data accessible. Usually,
we use different fonts and colors to prioritize text visually, but how can we
achieve the same impact for assistive technologies?

> To learn about the basics of accessibility in SwiftUI, take a look at my [
> “Accessibility in SwiftUI” ](/2019/09/10/accessibility-in-swiftui/) post.

Fortunately, SwiftUI provides a way to generate customized accessibility
content with different importance using the brand new
_accessibilityCustomContent_ view modifier. Let’s take a look at how we can
use it.

    
    
    struct UserView: View {
        let user: User
    
        var body: some View {
            VStack(alignment: .leading) {
                Text(user.name)
                    .font(.headline)
                Text(user.address)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                Text(user.email)
                    .foregroundColor(.secondary)
                Text("Age: \(user.age)")
                    .foregroundColor(.secondary)
            }
            .accessibilityElement(children: .ignore)
            .accessibilityLabel(user.name)
            .accessibilityCustomContent("Age", "\(user.age)")
            .accessibilityCustomContent("Email", user.email, importance: .high)
            .accessibilityCustomContent("Address", user.address, importance: .default)
        }
    }
    

Here we add a bunch of _accessibilityCustomContent_ view modifiers to define
custom accessibility content with various priorities. The
_accessibilityCustomContent_ view modifier has three parameters:

  1. The first one is the localized label for your custom content that VoiceOver uses to announce. 
  2. The second one is the localized label or string value presenting custom content. 
  3. The third one is the importance level of your custom content. It can be _default_ or _high_ . VoiceOver reads content with high importance immediately, while the content with default importance is spoken only in verbose mode when the user uses vertical swipes to access more data. 

The _accessibilityCustomContent_ view modifier allows us to prioritize data
for assistive technologies. For example, VoiceOver reads the data with _high_
importance immediately and enables the user to access data with _default_
importance as needed using vertical swipes.

You can use as many _accessibilityCustomContent_ view modifiers as needed to
present a massive subset of your data. Remember that you can also replace and
override data or importance by introducing _accessibilityCustomContent_ view
modifiers with the same label.

An excellent way to keep your custom accessibility content labels consistent
across the large codebase is using the _AccessibilityCustomContentKey_ type.
You can use an instance of it as the first parameter of the
_accessibilityCustomContent_ view modifier.

    
    
    extension AccessibilityCustomContentKey {
        static let age = AccessibilityCustomContentKey("Age")
        static let email = AccessibilityCustomContentKey("Email")
        static let address = AccessibilityCustomContentKey("Address")
    }
    
    struct UserView: View {
        let user: User
    
        var body: some View {
            VStack(alignment: .leading) {
                Text(user.name)
                    .font(.headline)
                Text(user.address)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                Text(user.email)
                    .foregroundColor(.secondary)
                Text("Age: \(user.age)")
                    .foregroundColor(.secondary)
            }
            .accessibilityElement(children: .ignore)
            .accessibilityLabel(user.name)
            .accessibilityCustomContent(.age, "\(user.age)")
            .accessibilityCustomContent(.email, user.email, importance: .high)
            .accessibilityCustomContent(.address, user.address, importance: .default)
        }
    }
    

In the example above, we define a few shortcuts for our custom accessibility
content keys and use them in conjunction with the _accessibilityCustomContent_
view modifier.

Today we learned how to use the _accessibilityCustomContent_ view modifier to
make our apps more accessible by prioritizing our data for assistive
technologies and allowing user access as more details as needed. I hope you
enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

