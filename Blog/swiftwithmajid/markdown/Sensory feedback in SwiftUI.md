##  Sensory feedback in SwiftUI

10 Oct 2023

SwiftUI introduced the new _sensoryFeedback_ view modifier, allowing us to
play haptic feedback on all Apple platforms. This week, we will learn how to
use the _sensoryFeedback_ modifier to give haptic feedback on different
actions in our apps.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

All we need to play haptic feedback in a SwiftUI view is to attach the
_sensoryFeedback_ view modifier with two parameters. The first defines a
feedback style, and the second is a trigger value.

    
    
    struct ContentView: View {
        @State private var store = Store()
        
        var body: some View {
            NavigationStack {
                List(store.results, id: \.self) { result in
                    Text(result)
                }
                .searchable(text: $store.query)
                .sensoryFeedback(.success, trigger: store.results)
            }
        }
    }
    

As you can see in the example above, we use the _sensoryFeedback_ view
modifier with _success_ style. We also define the _results_ property of the
store as a trigger. It means SwiftUI will play the success-styled haptic
feedback whenever store results change.

SwiftUI provides a bunch of predefined feedback styles like _success_ ,
_warning_ , _error_ , _selection_ , _increase_ , _decrease_ , _start_ , _stop_
, _alignment_ , _levelChange_ , _impact_ , etc.

    
    
    struct ContentView: View {
        @State private var trigger = false
        
        var body: some View {
            NavigationStack {
                Button("Action") {
                    // do something
                    trigger.toggle()
                }
                .sensoryFeedback(
                    .impact(weight: .heavy, intensity: 0.9),
                    trigger: trigger
                )
            }
        }
    }
    

As you can see, the _impact_ style allows us to tune the _weight_ and
_intensity_ of the feedback. Remember that it is always better to use the
predefined style and customize the haptic feedback for super custom cases.

    
    
    struct ContentView: View {
        @State private var store = Store()
        
        var body: some View {
            NavigationStack {
                List(store.results, id: \.self) { result in
                    Text(result)
                }
                .searchable(text: $store.query)
                .sensoryFeedback(trigger: store.results) { oldValue, newValue in
                    return newValue.isEmpty ? .error : .success
                }
            }
        }
    }
    

Another variant of the _sensoryFeedback_ view modifier allows us to choose a
particular feedback style depending on the trigger value. Here, we play
_success_ feedback whenever our store contains results and play _error_
feedback whenever results are empty.

    
    
    struct ContentView: View {
        @State private var store = Store()
        
        var body: some View {
            NavigationStack {
                List(store.results, id: \.self) { result in
                    Text(result)
                }
                .searchable(text: $store.query)
                .sensoryFeedback(.success, trigger: store.results) { oldValue, newValue in
                    return newValue.isEmpty
                }
            }
        }
    }
    

SwiftUI also provides an option to define a condition on trigger value,
deciding whenever it should play or not a predefined feedback style.

This week, we learned how to use the new _sensoryFeedback_ view modifier to
play haptic feedback in our SwiftUI views. Remember that you shouldn’t
overwhelm the user with haptics. Use them to improve accessibility and
significant task results. I hope you enjoy the post. Feel free to follow me on
[ Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

