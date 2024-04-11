##  Accessibility rotors in SwiftUI

14 Sep 2021

SwiftUI Release 3 contains many new APIs that we can utilize to improve
accessibility in our apps, and one of them is the new _accessibilityRotor_
view modifier. This week we will learn how to use the _accessibilityRotor_
view modifier to provide custom VoiceOver navigation using rotors.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

Usually, we navigate through the app using the left and right swipes while
VoiceOver is on. But sometimes, we need a custom path for navigation through a
specific collection of elements. A particular group of elements is called a
custom rotor. You can create as many as you need custom rotors in your app.

To use the rotor, rotate two fingers on your iOS device’s screen as if you’re
turning a dial. VoiceOver will say the first rotor option. Keep rotating your
fingers to hear more options. Lift your fingers to choose an option. Then
flick your finger up or down on the screen to navigate through it.

####  SwiftUI custom rotors API

Assume that we are working on a screen that provides information about health
trends. There is a long list of different trends, including positive,
negative, and constant results. Negative trends are the things the user should
focus on improving. That’s why we should build a custom rotor to navigate only
through negative trends. Let’s start by introducing the _Trend_ model and the
_TrendsView_ .

    
    
    import SwiftUI
    
    struct Trend: Identifiable {
        let id = UUID()
        let message: String
        let isPositive: Bool
    }
    
    struct TrendView: View {
        let trend: Trend
    
        var body: some View {
            HStack {
                Image(systemName: trend.isPositive ? "chevron.up" : "chevron.down")
                    .accessibilityElement()
                    .accessibilityLabel(trend.isPositive ? "positive" : "negative")
                Text(trend.message)
            }.accessibilityElement(children: .combine)
        }
    }
    

The code above is super simple. Please look at how we use the
_accessibilityElement_ view modifier to make _TrendView_ accessible and
combine all the children’s information.

> To learn about the basics of accessibility in SwiftUI, take a look at my [
> “Accessibility in SwiftUI” ](/2019/09/10/accessibility-in-swiftui/) post.
    
    
    struct TrendsView: View {
        let trends: [Trend]
    
        var body: some View {
            List {
                ForEach(trends, id: \.id) { trend in
                    TrendView(trend: trend)
                }
            }
            .accessibilityRotor("Negative trends") {
                ForEach(trends, id: \.id) { trend in
                    if !trend.isPositive {
                        AccessibilityRotorEntry(trend.message, id: trend.id)
                    }
                }
            }
        }
    }
    

Here we have the _TrendsView_ that displays the list of trends. We use the
_accessibilityRotor_ view modifier to create a custom rotor called “Negative
trends”. As soon as the user focuses on the list, VoiceOver suggests accessing
the negative trends rotor.

The first parameter of _accessibilityRotor_ view modifier is a label. You can
use _String, LocalizedStringKey, or Text_ view as a label. VoiceOver uses the
title to inform a user about a custom rotor.

The second parameter is the _AccessibilityRotorContentBuilder_ closure. The
_AccessibilityRotorContentBuilder_ function builder is very similar to
_ViewBuilder_ , but instead of building views, it creates
_AccessibilityRotorContent_ .

_AccessibilityRotorContent_ is also identical to _View_ protocol, but it
describes the content of the rotor. SwiftUI types like _ForEach_ and _Group_
conform both to _View_ and _AccessibilityRotorContent_ protocols. That’s why
we can use them both inside _ViewBuilder_ and
_AccessibilityRotorContentBuilder_ closures.

The last piece is the _AccessibilityRotorEntry_ conforming to
_AccessibilityRotorContent_ and allowing us to use it inside a _ForEach_ or
_Group_ . We use it to create a rotor entry and bind it to a SwiftUI view
using an ID. This is the point where all the magic takes place. We have two
_ForEach_ instances, and SwiftUI is smart enough to match the IDs inside
_ForEach_ and bind rotor entries to the views with the same IDs.

####  accessibilityRotorEntry view modifier

The approach above works like a charm, but we can gain more control over
binding rotor entry to a view using the _accessibilityRotorEntry_ view
modifier.

    
    
    struct TrendsView: View {
        let trends: [Trend]
    
        @Namespace private var customRotorNamespace
    
        var body: some View {
            List {
                ForEach(trends, id: \.id) { trend in
                    VStack {
                        TrendView(trend: trend)
                            .accessibilityRotorEntry(id: trend.id, in: customRotorNamespace)
                        Text(trend.notes)
                    }
                }
            }
            .accessibilityRotor("Negative trends") {
                ForEach(trends, id: \.id) { trend in
                    if !trend.isPositive {
                        AccessibilityRotorEntry(trend.message, trend.id, in: customRotorNamespace) 
                    }
                }
            }
        }
    }
    

In this case, we use the _accessibilityRotorEntry_ view modifier to bind a
rotor entry id to a view explicitly. It allows us to ignore IDs from _ForEach_
and can be very helpful in situations where we don’t have ForEach or don’t
need to include the whole child of _ForEach_ into the rotor, like in our
example.

####  Preparing rotor entries

As a bonus, the _AccessibilityRotorEntry_ type allows us to provide a closure
to run when the user navigates to a particular rotor entry. For example, we
can scroll to the specific list item if it is not visible when navigating to
that item using rotors.

    
    
    struct TrendsView: View {
        let trends: [Trend]
    
        @Namespace private var customRotorNamespace
    
        var body: some View {
            ScrollViewReader { scrollView in
                List {
                    ForEach(trends, id: \.id) { trend in
                        TrendView(trend: trend)
                            .accessibilityRotorEntry(id: trend.id, in: customRotorNamespace)
                            .id(trend.id)
                    }
                }
                .accessibilityRotor("Negative trends") {
                    ForEach(trends, id: \.id) { trend in
                        if !trend.isPositive {
                            AccessibilityRotorEntry(trend.message, trend.id, in: customRotorNamespace) {
                                scrollView.scrollTo(trend.id)
                            }
                        }
                    }
                }
            }
        }
    }
    

####  TextEditor Rotors

The new accessibility rotors API is robust and allows us to navigate even
through text in _TextEditor_ . We can mark particular parts of our text
content and navigate between them inside the _TextEditor_ .

    
    
    struct ContentEditor: View {
        @Binding var content: Content
    
        var body: some View {
            TextEditor(text: $content.text)
                .accessibilityRotor("Emails", textRanges: content.emailRanges)
                .accessibilityRotor("Links", textRanges: content.linkRanges)
        }
    }
    

####  Conclusion

SwiftUI Release 3 has done great work in the area of accessibility. Now we can
use all these new APIs to build super accessible apps. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

