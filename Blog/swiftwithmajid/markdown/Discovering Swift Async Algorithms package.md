##  Discovering Swift Async Algorithms package

26 Feb 2024

Another week on a series of posts about discovering Swift packages. This week,
we will discover the Swift Async Algorithms package, allowing us to completely
switch from the Combine framework to the Swift Concurrency feature with
async/await. We will learn what the Swift Async Algorithms package offers to
eliminate the Combine framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The [ Swift Async Algorithms package ](https://github.com/apple/swift-async-
algorithms) is another package that Apple maintains and provides us. You can
always become a part of this great community by contributing to the package on
GitHub.

####  Combining

The Swift Async Algorithms package offers a set of functions allowing us to
combine two or three async sequences into a single sequence. For example, you
can merge two async sequences in a single one and observe values from the
resulting sequence.

    
    
    @Observable final class CalendarStore {
        private(set) var events: [Event] = []
        
        func observeEvents() async {
            let dayChanges = NotificationCenter.default.notifications(named: .NSCalendarDayChanged)
            let timezoneChanges = NotificationCenter.default.notifications(named: .NSSystemTimeZoneDidChange)
            
            for await change in merge(dayChanges, timezoneChanges) {
                await fetchEvents()
            }
        }
        
        func fetchEvents() async {
            // ...
        }
    }
    

As you can see in the example above, we use the _merge_ function that allows
us to create a single sequence then observe day and timezone changes at once.
The Swift Async Algorithms package provides not only _merge_ functions but
also _combineLatest_ , _zip_ , _chain_ , and _join_ .

    
    
    @Observable final class CalendarStore {
        private(set) var events: [Event] = []
        
        func observeEvents() async {
            let dayChanges = NotificationCenter.default.notifications(named: .NSCalendarDayChanged)
            let timezoneChanges = NotificationCenter.default.notifications(named: .NSSystemTimeZoneDidChange)
            
            for await change in zip(dayChanges, timezoneChanges) {
                await fetchEvents()
            }
        }
        
        func fetchEvents() async {
            // ...
        }
    }
    

The Swift Async Algorithms package also includes grouping and filtering
operators from the Swift Algorithms package but applies to async sequences
like _compacted_ for filtering _nil_ values or chunking and removing
duplicates.

> To learn more about the Swift Algorithms package, take a look at my [
> “Discovering Swift Algorithms package” ](/2024/02/13/discovering-swift-
> algorithms-package/) post.

####  Time manipulations

The Swift Async Algorithms package introduces a few operators, allowing us to
manipulate the sequence using time, similar to the Combine framework. For
example, you can debounce and throttle async sequences.

    
    
    @Observable final class CalendarStore {
        private(set) var events: [Event] = []
        
        func observeEvents() async {
            let dayChanges = NotificationCenter.default.notifications(named: .NSCalendarDayChanged)
            let timezoneChanges = NotificationCenter.default.notifications(named: .NSSystemTimeZoneDidChange)
            
            for await change in merge(dayChanges, timezoneChanges).debounce(for: .seconds(1)) {
                await fetchEvents()
            }
        }
        
        func fetchEvents() async {
            // ...
        }
    }
    

As you can see in the example above, we use the _debounce_ function to wait
for a particular period of time before emitting a value. Another helpful type
that we have in The Swift Async Algorithms package is _AsyncTimerSequence_ .
It emits the current date at a given interval.

    
    
    @Observable final class CalendarStore {
        private(set) var events: [Event] = []
        
        func observeEvents() async {
            let dayChanges = NotificationCenter.default.notifications(named: .NSCalendarDayChanged)
            let timezoneChanges = NotificationCenter.default.notifications(named: .NSSystemTimeZoneDidChange)
            
            let timer = AsyncTimerSequence(interval: .seconds(5), clock: .suspending)
            for await interval in timer {
                await fetchEvents(in: Date.now)
            }
        }
        
        func fetchEvents(in date: Date) async {
            // ...
        }
    }
    

####  AsyncChannel

The _AsyncChannel_ type allows us to replace passthrough subjects from the
Combine framework. It is a great way to bridge the part of the code that
doesn’t support async context with the async context in your app.

    
    
    let channel = AsyncChannel<UUID>()
    
    Task {
        for await id in channel {
            print(id)
        }
    }
    
    await channel.send(UUID())
    await channel.send(UUID())
    channel.finish()
    

As you can see in the example above, we use the _send_ function on an instance
of the _AsyncChannel_ type to emit values. Conversely, the _AsyncChannel_
conforms to the _AsyncSequence_ protocol to support for-each loop with the
_await_ keyword. Remember to call the _finish_ function on the channel to
close the sequence.

    
    
    let channel = AsyncThrowingChannel<UUID>()
    
    Task {
        for await id in channel {
            print(id)
        }
    }
    
    await channel.send(UUID())
    await channel.fail(SomeError())
    

There is also the _AsyncThrowingChannel_ type with a similar functionality
supporting failing with errors. Whenever you need to close the channel with an
error, you can use the _fail_ function on an instance of the
_AsyncThrowingChannel_ type.

####  Conclusion

Today we discovered the Swift Async Algorithms package, allowing us to move
completely from the Combine framework to the Swift Concurrency feature. I hope
you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

