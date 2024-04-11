##  Structural identity in SwiftUI

09 Dec 2021

Structural identity is the type of identity that SwiftUI uses to understand
your views without an explicit identifier by using your layout description.
This week we will learn how to improve performance and eliminate unwanted
animations by using inert view modifiers in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Structural identity

Structural identity is how SwiftUI understands your view hierarchy and
recognizes particular views without specific identifiers. Let’s look at the
quick examples that demonstrate the logic behind the structural identity.

    
    
    struct UserView: View {
        let user: User?
    
        var body: some View {
            if let user = user {
                LoggedUser(user: user)
            } else {
                AnonymousUserView()
            }
        }
    }
    
    print(Mirror(reflecting: UserView(user: nil).body))
    // Mirror for _ConditionalContent<LoggedUser, AnonymousUserView>
    

As you can see in the example above, SwiftUI creates an instance of
__ConditionalContent_ view that uses some condition to present one or another
view. In our case, __ConditionalContent_ view uses **if let** binding to
decide which views it has to show. SwiftUI destroys and creates the views
whenever the condition changes. This process deallocates the destroyed view’s
state and uses animation to remove the destroyed view.

    
    
    struct AchievementView: View {
        let isEnabled: Bool
    
        var body: some View {
            if isEnabled {
                ComplexView()
            } else {
                ComplexView()
                    .disabled(true)
            }
        }
    }
    

In the current example, we use the _if_ statement to enable or disable the
view conditionally. We still use branching via _if_ statement, and SwiftUI
will destroy and create views accordingly. It might look correct, but we lose
the state of the instance of _ComplexView_ during the condition change because
SwiftUI recreates view inside the branches of the _if_ statement, and more, we
get unwanted animation while swapping these views.

Let’s solve our issue by removing the _if_ statement and moving the condition
inside the _disabled_ view modifier.

    
    
    struct AchievementView: View {
        let isEnabled: Bool
    
        var body: some View {
            ComplexView()
                .disabled(isEnabled ? false : true)
        }
    }
    

In the example above, we don’t have the _if_ statement. We inline the
condition inside the _disable_ view modifier, which allows us to keep the
structural identity of our view. SwiftUI understands that it is the same view
but with a different value for the _disabled_ view modifier.

Remember that you should use branching via **if** or **switch** statement only
when you need to present different views. Always try to inline your conditions
inside the view modifiers to keep your structural identity.

> To learn more why SwiftUI uses structural identity, take a look at my [ “You
> have to change mindset to use SwiftUI” ](/2019/11/19/you-have-to-change-
> mindset-to-use-swiftui/) post.

####  Inert modifiers

SwiftUI framework is smart enough to understand and optimize your view
hierarchy. It provides us with a set of inert view modifiers which doesn’t
affect view tree, and you can use them for free. Let’s take a look at some of
them in the example below.

    
    
    struct AchievementView: View {
        let isEnabled: Bool
    
        var body: some View {
            ComplexView()
                .opacity(isEnabled ? 1 : 0)
                .padding(isEnabled ? 8 : 0)
        }
    }
    

There is no changes in the view tree when you set the padding to 0 or opacity
to 1. SwiftUI understands that and doesn’t apply these view modifiers. That’s
why we call them inert view modifiers. Try to use them as much as possible to
improve the performance of your view and remove unwanted transitions.

> To learn more tips and tricks dedicated to view composition in SwiftUI, take
> a look at my [ “View composition in SwiftUI” ](/2019/10/30/view-composition-
> in-swiftui/) post.

####  Conclusion

This week we learned about structural identity in SwiftUI. It is crucial to
understand how it works to build great and performant views with SwiftUI. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

