##  Mastering Dynamic Island in SwiftUI

28 Sep 2022

In the previous post, we talked about live activity widgets displaying your
app’s ongoing events. Live activity widgets can utilize the dynamic island of
the iPhone 14 Pro. In this post, we will discuss possible configurations and
customization points of the dynamic island feature using the new API available
in the WidgetKit framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The WidgetKit framework provides us with a particular type of configuration
called _ActivityConfiguration_ , allowing us to define a live activity widget.

    
    
    @available(iOSApplicationExtension 16.1, *)
    struct FastingActivityWidget: Widget {
        var body: some WidgetConfiguration {
            ActivityConfiguration(for: FastingAttributes.self) { context in
                LiveActivityView(context: context)
                    .padding(.horizontal)
            } dynamicIsland: { context in
                DynamicIsland {
                    DynamicIslandExpandedRegion(.leading) {
                        LiveActivityView(context: context)
                    }
                } compactLeading: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                } compactTrailing: {
                    Text(verbatim: context.state.progress.formatted(.percent.precision(.fractionLength(0))))
                        .foregroundColor(context.state.stage?.color)
                } minimal: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                }
            }
        }
    }
    

We use the _ActivityConfiguration_ type to define a SwiftUI view to display on
the lock screen. In this case, we will use our custom _LiveActivityView_ . We
also provide a dynamic island layout configuration to display on iPhone 14
Pro.

> To learn about the basics of live activity widgets, take a look at my
> dedicated [ “Displaying live activities in iOS 16” ](/2022/09/21/displaying-
> live-activities-in-ios16/) post.

WidgetKit has a particular _DynamicIsland_ type allowing us to specify how we
want to use the dynamic island layout. The _DynamicIsland_ type is not a
SwiftUI view but requires us to provide views for compact leading and compact
trailing, expanded, and minimal cases.

Whenever your app is the only app running live activity widget at the moment,
the system displays both compact leading and compact trailing views
accordingly.

![dynamic-island-compact](/public/dynamic-island-compact.png)

The system uses minimal view whenever there is more than one live activity
widget at the moment and displays it as detached trailing view.

![dynamic-island-minimal](/public/dynamic-island-minimal.png)

The expanded view is used when the user uses a long press gesture to expand
the dynamic island.

![dynamic-island-expanded](/public/dynamic-island-expanded.png)

The expanded dynamic island divides its space into four areas and allows us to
control where we want to place the content. We also can use the _priority_
parameter to enable the system to prioritize the views while sizing them.

    
    
    @available(iOSApplicationExtension 16.1, *)
    struct FastingActivityWidget: Widget {
        var body: some WidgetConfiguration {
            ActivityConfiguration(for: FastingAttributes.self) { context in
                LiveActivityView(context: context)
            } dynamicIsland: { context in
                DynamicIsland {
                    DynamicIslandExpandedRegion(.leading, priority: 1) {
                        LiveActivityView(context: context)
                    }
                    
                    DynamicIslandExpandedRegion(.trailing) {
                        LiveActivityView(context: context)
                    }
                    
                    DynamicIslandExpandedRegion(.center) {
                        LiveActivityView(context: context)
                    }
                    
                    DynamicIslandExpandedRegion(.bottom) {
                        LiveActivityView(context: context)
                    }
                } compactLeading: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                } compactTrailing: {
                    Text(verbatim: context.state.progress.formatted(.percent.precision(.fractionLength(0))))
                        .foregroundColor(context.state.stage?.color)
                } minimal: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                }
            }
        }
    }
    

Sometimes we might have too wide content in the leading view that doesn’t fit
into the available space. In this case, we can use the _dynamicIsland_ view
modifier to move the leading view below the True Depth camera.

![dynamic-island-expanded-wide](/public/dynamic-island-expanded-wide.png)

    
    
    @available(iOSApplicationExtension 16.1, *)
    struct FastingActivityWidget: Widget {
        var body: some WidgetConfiguration {
            ActivityConfiguration(for: FastingAttributes.self) { context in
                LiveActivityView(context: context)
            } dynamicIsland: { context in
                DynamicIsland {
                    DynamicIslandExpandedRegion(.leading, priority: 1) {
                        LiveActivityView(context: context)
                            .dynamicIsland(verticalPlacement: .belowIfTooWide)
                    }
                } compactLeading: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                } compactTrailing: {
                    Text(verbatim: context.state.progress.formatted(.percent.precision(.fractionLength(0))))
                        .foregroundColor(context.state.stage?.color)
                } minimal: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                }
            }
        }
    }
    

Another customization point is the background color of compact and minimal
views. By default, the system uses black color to fill the compact and minimal
views, but we can use the _keylineTint_ view modifier to change the color.

    
    
    @available(iOSApplicationExtension 16.1, *)
    struct FastingActivityWidget: Widget {
        var body: some WidgetConfiguration {
            ActivityConfiguration(for: FastingAttributes.self) { context in
                LiveActivityView(context: context)
            } dynamicIsland: { context in
                DynamicIsland {
                    DynamicIslandExpandedRegion(.leading, priority: 1) {
                        LiveActivityView(context: context)
                            .dynamicIsland(verticalPlacement: .belowIfTooWide)
                    }
                } compactLeading: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                } compactTrailing: {
                    Text(verbatim: context.state.progress.formatted(.percent.precision(.fractionLength(0))))
                        .foregroundColor(context.state.stage?.color)
                } minimal: {
                    Image(systemName: "circle")
                        .foregroundColor(.green)
                }
                .keylineTint(.white)
            }
        }
    }
    

Today we learned how to use the dynamic island feature to display live
activities from your app on iPhone 14 Pro. I hope you enjoy the post. Feel
free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this article. Thanks for reading, and see you next week!

