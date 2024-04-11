##  The difference between @StateObject, @EnvironmentObject, and
@ObservedObject in SwiftUI

02 Jul 2020

This week I decided to share as much as I can about data flow in SwiftUI. In
this post, we will discuss the difference between @ _StateObject_ , @
_EnvironmentObject_ , and @ _ObservedObject_ property wrappers. I know that
this is the most confusing topic in SwiftUI for newcomers.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Why SwiftUI does need property wrappers?

SwiftUI uses immutable struct types to describe the view hierarchy. All the
views that SwiftUI provides are immutable. That’s why SwiftUI gives us a bunch
of property wrappers to handle data mutations. Property wrappers allow us to
declare them inside SwiftUI views but store the data outside of the view
declaring it.

####  @StateObject

@ _StateObject_ is the new property wrapper that initializes the instance of a
class that conforms to _ObservableObject_ protocol and store it inside the
SwiftUI framework’s internal memory. SwiftUI creates @ _StateObject_ only once
for every container that declares it and keeps it outside of view lifecycle.
Let’s look at some examples where we use @ _StateObject_ to keep the whole
app’s state.

    
    
    import SwiftUI
    
    @main
    struct CardioBotApp: App {
        @StateObject var store = Store(
            initialState: AppState(),
            reducer: appReducer,
            environment: AppEnvironment(service: HealthService())
        )
    
        var body: some Scene {
            WindowGroup {
                RootView().environmentObject(store)
            }
        }
    }
    

As you can see, @ _StateObject_ perfectly fits to store the whole app state
and share it with different scenes or views of your app. SwiftUI will store it
in special framework memory to keep your data in a safe place outside of scene
or view lifecycle.

> To learn more about using a single state container, take a look at my [
> “Redux-like state container in SwiftUI. Basics.” ](/2019/09/18/redux-like-
> state-container-in-swiftui/) post.

####  @ObservedObject

@ _ObservedObject_ is another way to subscribe and keep track of changes in
_ObservableObject_ . SwiftUI doesn’t control the lifecycle of @
_ObservedObject_ , and you have to manage it yourself. @ _ObservedObject_
perfectly fits a case where you have an _ObservableObject_ stored by @
_StateObject_ , and you want to share it with any reusable view.

    
    
    struct CalendarContainerView: View {
        @ObservedObject var store: Store<CalendarState, CalendarAction>
        let interval: DateInterval
    
        var body: some View {
            CalendarView(interval: interval) { date in
                DateView(date: date) {
                    self.view(for: date)
                }
            }.navigationBarTitle("calendar", displayMode: .inline)
        }
    }
    

I mention reusable views because I use _CalendarContainerView_ in multiple
places in my app, and I don’t want to make it dependent on the environment. I
use @ _ObservedObject_ to explicitly indicate the data used by the view in
that particular case.

    
    
    NavigationLink(
        destination: CalendarContainerView(
            store: transformedStore,
            interval: .twelveMonthsAgo
        )
    ) {
        Text("Calendar")
    }
    

> To learn more about using container views, take a look at my [ “Redux-like
> state container in SwiftUI. Container Views.” ](/2019/10/02/redux-like-
> state-container-in-swiftui-part3/) post.

####  @EnvironmentObject

@ _EnvironmentObject_ is an excellent way to implicitly inject an instance of
a class that conforms to _ObservableObject_ into a part of the view hierarchy.
Assume that you have a module in your app that contains 3-4 screens, and all
of them use the same view model. If you don’t want to pass the same view model
explicitly from one view to another, then @ _EnvironmentObject_ is all you
need. Let’s take a look at how we can use it.

    
    
    @main
    struct CardioBotApp: App {
        @StateObject var store = Store(
            initialState: AppState(),
            reducer: appReducer,
            environment: .production
        )
    
        var body: some Scene {
            WindowGroup {
                TabView {
                    NavigationView {
                        SummaryContainerView()
                            .navigationBarTitle("today")
                            .environmentObject(
                                store.derived(
                                    deriveState: \.summary,
                                    embedAction: AppAction.summary
                                )
                            )
                    }
    
                    NavigationView {
                        TrendsContainerView()
                            .navigationBarTitle("trends")
                            .environmentObject(
                                store.derived(
                                    deriveState: \.trends,
                                    embedAction: AppAction.trends
                                )
                            )
                    }
                }
            }
        }
    }
    

In the example above, we inject the environment object into the view hierarchy
of _SummaryContainerView_ . SwiftUI will implicitly give access for inserted
environment objects to all child views that live inside _SummaryContainerView_
. We can quickly obtain and subscribe to injected environment objects using @
_EnvironmentObject_ property wrapper.

    
    
    struct SummaryContainerView: View {
        @EnvironmentObject var store: Store<SummaryState, SummaryAction>
    
        var body: some View {
            //......
        }
    }
    

I have to mention that @ _EnvironmentObject_ has the same lifecycle as @
_ObservedObject_ . It means that you can get a new environment object whenever
you create it inside a view that can be recreated by SwiftUI.

> To learn more about advanced techniques while using a single state
> container, take a look at my [ “Redux-like state container in SwiftUI. Best
> practices.” ](/2019/09/25/redux-like-state-container-in-swiftui-part2/)
> post.

####  Conclusion

Today we talked about the differences between @ _StateObject_ , @
_EnvironmentObject_ , and @ _ObservedObject_ property wrappers. I hope this
post makes it easier to understand which property wrapper fits best your case.
Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for reading, and see you next week!

