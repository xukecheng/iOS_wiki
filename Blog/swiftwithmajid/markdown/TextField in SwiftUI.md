##  TextField in SwiftUI

26 Feb 2020

This week I want to talk to you about a _TextField_ component in SwiftUI. It
might look like an elementary tutorial, but _TextField_ has pretty exciting
features like out of the box formatting that we don’t have in _UIKit_ . But
let’s start with the basics of the _TextField_ component.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

As you might know, we can use _TextField_ for user input. All we need to do is
to create a _TextField_ and assign it to any _Binding_ of a _String_ value.
Let’s take a look at a very quick example.

    
    
    struct ContentView: View {
        @State private var text = ""
    
        var body: some View {
            TextField("type something...", text: $text)
        }
    }
    

In the example above, we create a _TextField_ with a placeholder and bind it
to a state variable. Pretty easy, right? _TextField_ also provides callbacks
that we might need to handle during user input.

    
    
    struct ContentView: View {
        @State private var text = ""
    
        var body: some View {
            TextField(
                "type something...",
                text: $text,
                onEditingChanged: { _ in print("changed") },
                onCommit: { print("commit") }
            )
        }
    }
    

As you can see in the example above, _TextField_ allows us to handle
_onEditingChanged_ and _onCommit_ events. Let’s learn what the difference
between them. _TextField_ calls _onEditingChanged_ closure whenever the user
starts or finishes editing text. It also passes a boolean value that describes
a starting or finishing event. Whenever a user performs an action like
pressing the return key, _TextField_ calls _onCommit_ closure.

####  TextField formatters

OK, we learned basics, and now we can move to a more interesting feature of
_TextFields_ . You might be noticed that _TextField_ has a few overloads that
accept _Formatter_ . These overloads allow us to bind a _TextField_ to raw
data and present it after converting to a string by using selected _Formatter_
instance. Let’s take a look at a quick example that will help us to understand
how it works.

    
    
    extension NumberFormatter {
        static var currency: NumberFormatter {
            let formatter = NumberFormatter()
            formatter.numberStyle = .currency
            return formatter
        }
    }
    
    struct ContentView: View {
        @State private var price = 99
    
        var body: some View {
            TextField(
                "type something...",
                value: $price,
                formatter: NumberFormatter.currency
            )
        }
    }
    

_TextField_ uses provided _Formatter_ while converting between the string that
user edits and the underlying raw value. In case when _Formatter_ is unable to
perform a conversion, the value will not be modified. Try to type some letters
that _Formatter_ is not able to convert to see what will happen.

####  New Formatter API

Swift Foundation provides us new Formatter API, which is available on iOS 15
and macOS 12. The new Formatter API allows us quickly build reusable
formatters using the builder design pattern. Fortunately, _TextField_ supports
the new API.

    
    
    @MainActor final class InsightsStore: ObservableObject {
        @Published private(set) var bodyFatUnit = HKUnit.percent()
        @Published var bodyFat: Double?
        
        func save() async {
        // ...
        }
    }
    
    struct BodyFatLoggingView: View {
        @ObservedObject var store: InsightsStore
        @Environment(\.dismiss) private var dismiss
        
        var body: some View {
            Form {
                Section {
                    HStack {
                        Text(store.bodyFatUnit.unitString)
                        TextField(
                            "bodyFat",
                             value: $store.bodyFat,
                             format: .percent.precision(.fractionLength(0...1))
                        )
                            .keyboardType(.numbersAndPunctuation)
                            .multilineTextAlignment(.trailing)
                    }
                }
                
                Section {
                    Button("save") {
                        Task {
                            await store.saveBodyFat()
                            dismiss()
                        }
                    }
                }
            }
        }
    }
    

####  Styling

SwiftUI provides us a few styles and the _textFieldStyle_ modifier that we can
use to apply styles to our _TextFields_ in the app. _textFieldStyle_ modifier
uses the environment to pass the style to every view inside the environment.
It looks very similar to the _buttonStyle_ modifier that discussed in the
previous post.

> To learn more about _buttonStyle_ modifier, take a look at my [ “Mastering
> buttons in SwiftUI post” ](/2020/02/19/mastering-buttons-in-swiftui/) .
    
    
    struct ContentView: View {
        @State private var text = ""
    
        var body: some View {
            TextField("type something...", text: $text)
                .textFieldStyle(RoundedBorderTextFieldStyle())
        }
    }
    

SwiftUI has a _TextFieldStyle_ protocol that we can use to provide styling to
our _TextFields_ . Let’s take a look at how we can use it.

    
    
    struct SuperCustomTextFieldStyle: TextFieldStyle {
        func _body(configuration: TextField<_Label>) -> some View {
            configuration
                .padding()
                .border(Color.accentColor)
        }
    }
    
    struct ContentView: View {
        @State private var text = ""
    
        var body: some View {
            TextField("type something...", text: $text)
                .textFieldStyle(SuperCustomTextFieldStyle())
        }
    }
    

It looks like there is some compiler magic behind this protocol because it
works with __body_ function, which is not a part of _TextFieldStyle_ .

> SwiftUI uses environment to pass system-wide and application-related
> information. You can also populate environment with your custom objects. To
> learn more about environment, take a look at my [ “The power of Environment
> in SwiftUI” ](/2019/08/21/the-power-of-environment-in-swiftui/) post.

####  Conclusion

This week we learned the things behind the _TextField_ component. It provides
us an interesting raw data formatting feature that we don’t have in _UIKit_ .
I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

