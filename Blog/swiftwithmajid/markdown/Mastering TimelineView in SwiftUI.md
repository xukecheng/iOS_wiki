##  Mastering TimelineView in SwiftUI

18 May 2022

TimelineView is a SwiftUI view type that updates its body according to a
provided schedule. We used to see SwiftUI views updating its body whenever the
data it presents changes. _TimelineView_ doesn’t follow this rule and allows
us to build a super-custom schedule to update its content in a precise way. We
will learn how to use _TimelineView_ to create time-based views this week.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Basics

_TimelineView_ reevaluates its body on the schedule we provide. Let’s look at
the quick example where we draw an animated circle for a minute.

    
    
    struct ContentView: View {
        var body: some View {
            TimelineView(.animation) { context in
                let value = secondsValue(for: context.date)
    
                Circle()
                    .trim(from: 0, to: value)
                    .stroke()
            }
        }
    
        private func secondsValue(for date: Date) -> Double {
            let seconds = Calendar.current.component(.second, from: date)
            return Double(seconds) / 60
        }
    }
    

In the example above, we use _TimelineView_ with the _animation_ schedule. The
_animation_ schedule is the system-provided scheduler that uses animation
duration on the current platform and reevaluates its body very often to
provide a nice transition. The second parameter is the _ViewBuilder_ closure
defining a view that _TimelineView_ should draw. It also takes the single
parameter called _context_ . The _context_ contains the date from the
scheduler that triggers the update. In our example, we use the _date_ field to
draw the circle.

> To learn more about how SwiftUI updates views, take a look at my [ “You have
> to change mindset to use SwiftUI”
> ](https://swiftwithmajid.com/2019/11/19/you-have-to-change-mindset-to-use-
> swiftui/) post.

####  Cadence

The second field of the _Context_ type is the cadence. The cadence represents
the rate at which _TimelineView_ updates, and it might change many times
during the view’s lifecycle. For example, running the _TimelineView_ on Apple
Watch might decrease cadence while the user lowers the wrist. Fortunately, the
_Cadence_ type conforms to _Comparable_ protocol, and we can easily compare
them.

    
    
    struct ContentView: View {
        var body: some View {
            TimelineView(.animation) { context in
                let date = context.date
                let value = context.cadence <= .live ?
                    nanosValue(for: date): secondsValue(for: date)
    
                Circle()
                    .trim(from: 0, to: value)
                    .stroke()
            }
        }
    
        private func secondsValue(for date: Date) -> Double {
            let seconds = Calendar.current.component(.second, from: date)
            return Double(seconds) / 60
        }
    
        private func nanosValue(for date: Date) -> Double {
            let seconds = Calendar.current.component(.second, from: date)
            let nanos = Calendar.current.component(.nanosecond, from: date)
            return Double(seconds * 1_000_000_000 + nanos) / 60_000_000_000
        }
    }
    

Here we use the cadence parameter to understand how fluid our animation should
be. The _Cadence_ enum provides three cases: _live_ , _seconds_ , and
_minutes_ .

####  Schedulers

We touched on the basics of _TimelineView_ . Let’s move forward and learn
about schedulers provided by SwiftUI and how we can build a custom scheduler.
SwiftUI provides us with another two schedulers: _everyMinute_ and _periodic_
scheduler. The _everyMinute_ scheduler updates the timeline every minute. The
_periodic_ scheduler allows us to give a start date and interval, after which
another update event should be fired.

    
    
    struct ContentView: View {
        var body: some View {
            TimelineView(.periodic(from: .now, by: 5)) { context in
                let value = secondsValue(for: context.date)
    
                Circle()
                    .trim(from: 0, to: value)
                    .stroke()
            }
        }
    
        private func secondsValue(for date: Date) -> Double {
            let seconds = Calendar.current.component(.second, from: date)
            return Double(seconds) / 60
        }
    }
    

The periodic schedule is good enough to cover almost all the needed cases, but
we can also build a custom schedule. We need to create a type conforming to
the _TimelineSchedule_ protocol and implement a single requirement.

    
    
    final class DailySchedule: TimelineSchedule {
        typealias Entries = [Date]
    
        func entries(from startDate: Date, mode: Mode) -> Entries {
            (1...30).map { startDate.addingTimeInterval(Double($0 * 24 * 3600)) }
        }
    }
    
    extension TimelineSchedule where Self == DailySchedule {
        static var daily: Self { .init() }
    }
    
    struct ContentView: View {
        var body: some View {
            TimelineView(.daily) { context in
                let value = dayValue(for: context.date)
    
                Circle()
                    .trim(from: 0, to: value)
                    .stroke()
            }
        }
    
        private func dayValue(for date: Date) -> Double {
            let day = Calendar.current.component(.day, from: date)
            return Double(day) / 30
        }
    }
    

As you can see in the example above, we have a custom schedule that generates
a timeline from the starting point on a daily basis.

####  Conclusion

Today we learned how to use the TimelineView to build views updating with a
specific period. It might be helpful while creating timer apps or custom
animations. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

