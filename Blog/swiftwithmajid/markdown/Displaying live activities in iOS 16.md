##  Displaying live activities in iOS 16

21 Sep 2022

One of the most prominent features of iOS 16 is live activity widgets. iOS 16
allows us to display the live state of ongoing activities from our apps on the
lock screen or in the Dynamic Island of the new iPhone 14 Pro. This week we
will learn how to build live activity widgets for our apps using the new
ActivityKit framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

First, we should be aware of the limitations of live activities in iOS 16. It
will allow us to understand use cases where the live activity widget makes
sense. Live activity has eight hours before the system ends it. I hope Apple
will increase the lifetime of live activities by at least 24 hours. In this
case, we can display things like long flights, etc.

Live activity widgets use the WidgetKit framework to display information on
the lock screen or in the Dynamic Island of the iPhone 14 Pro. We can share
the code between home screen widgets and live activity widgets. The only
difference is the lifecycle. Live activity widgets don’t have a timeline
provider and should be managed from the app target using the ActivityKit
framework.

####  Data flow

Every live activity has two parts of data: static and dynamic. Static is not
going to change and is available whenever an activity starts. The dynamic part
is going to change during the live activity. In the case of a football match,
teams are static data because it is not going to change during the game. The
score is a dynamic part of the data and can change during the activity. The
dynamic portion of the data should not exceed 4kb. Let’s model our football
match using the new ActivityKit framework.

    
    
    import ActivityKit
    
    struct FootballMatch: ActivityAttributes {
        typealias ContentState = Score
    
        struct Score: Codable, Hashable {
            let score1: Int
            let score2: Int
        }
        
        let team1: String
        let team2: String
    }
    

The ActivityKit framework requires us to create a type conforming to the
_ActivityAttributes_ protocol. The type conforming to the _ActivityAttributes_
should provide static information about the activity and define the
_ContentState_ type containing the dynamic part of the data.

Your app must be in the foreground to start a live activity, and don’t forget
to add the **Supports Live Activities** key with **YES** value to the app
target’s _Info.plist_ . Now you can start a live activity using the following
code:

    
    
    let activity = try Activity.request(
        attributes: FootballMatch(
            team1: "AJAX",
            team2: "PSV"
        ),
        contentState: .init(
            score1: 0,
            score2: 0
        )
    )
    

As you can see in the example above, we request a live activity by providing
the initial attributes. Now we can hold the result of the live activity
request in the variable and update or end it whenever needed.

    
    
    // Update live activity
    Task {
        await activity.update(using: .init(score1: 1, score2: 0))
    }
    
    // End live activity
    Task {
        await activity.end(
            using: .init(score1: 1, score2: 0),
            dismissalPolicy: .immediate
        )
    }
    
    

You can use the BackgroundTasks framework or push notifications to update or
end your live activity without running the app in the foreground.

> To learn more about the BackgroundTasks framework, take a look at my [
> “Background tasks in SwiftUI” ](/2022/07/06/background-tasks-in-swiftui/)
> post.

####  Live activity presentation

We have to use the WidgetKit framework to display a live activity. WidgetKit
provides us with the particular _ActivityConfiguration_ type allowing us to
define a live activity widget.

    
    
    @available(iOSApplicationExtension 16.1, *)
    struct FastingActivityWidget: Widget {
        var body: some WidgetConfiguration {
            ActivityConfiguration(for: FastingAttributes.self) { context in
                LiveActivityView(context: context)
                    .padding(.horizontal)
            } dynamicIsland: { context in
                DynamicIsland {
                    DynamicIslandExpandedRegion(.center) {
                        LiveActivityView(context: context)
                    }
                } compactLeading: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                } compactTrailing: {
                    Text(verbatim: context.state.progress.formatted(.percent)
                        .foregroundColor(context.state.stage?.color)
                } minimal: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                }
            }
        }
    }
    

You should define the widget type using _ActivityConfiguration_ and add it to
your widget bundle. _ActivityConfiguration_ requires us to provide a view that
represents the activity on the lock screen and the Dynamic Island
configuration to display activity on the iPhone 14 Pro.

    
    
    @main struct FastBotWidgetBundle: WidgetBundle {
        var body: some Widget {
            FastBotWidget()
            
            if #available(iOS 16.1, *) {
                FastingActivityWidget()
            }
        }
    }
    

> Look at my dedicated [ “Building widgets in SwiftUI” ](/2020/09/09/building-
> widgets-in-swiftui/) post to learn more about the WidgetKit framework.

####  Conclusion

Today we learned how to build a live activity widget for iOS 16. In the next
post, I will try to cover the Dynamic Island configuration type allowing us to
layout our content in a few ways. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this article. Thanks for reading, and see you next week!

