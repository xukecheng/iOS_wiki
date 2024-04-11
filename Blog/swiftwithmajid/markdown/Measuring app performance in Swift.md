##  Measuring app performance in Swift

04 May 2022

The Unified Logging System is a great way to build a proper logging system
allowing you to understand different exceptional cases happening in your app.
But it is not limited only to logging. It also provides a way to measure
various events in your app. This week, we will learn how to use the Unified
Logging System to measure app performance.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Measuring app events

The Unified Logging System provides us with the Signpost API, which is a way
to measure various time intervals in your app. Let’s take a look at how we can
use it in a small example.

    
    
    @MainActor final class TimerStore: ObservableObject {
        private static let logger = Logger(
            subsystem: "com.aaplab.fastbot",
            category: "TimerStore"
        )
        private static let signposter = OSSignposter(logger: logger)
        
        @Published private(set) var accountStatus: CKAccountStatus = .couldNotDetermine
        @Published private(set) var recentFasting: Fasting? = nil
        
        private let service = CloudKitService()
        
        func fetchRecent() async {
            let signpostID = Self.signposter.makeSignpostID()
    
            let interval = Self.signposter.beginInterval("Fetching recent", id: signpostID)
            do {
                accountStatus = try await service.checkAccountStatus()
                recentFasting = try await service.fetchAllFastingRecords().last
                Self.signposter.endInterval("Fetching recent", interval)
            } catch {
                Self.signposter.endInterval("Fetching recent", interval)
            }
        }
    }
    

First, we need to import the _OSLog_ module that contains the Unified Logging
System API. Then we create an instance of the _OSSignposter_ type that we will
use to track event intervals. We use the _makeSignpostID_ function on the
_OSSignposter_ type to create a unique event identifier.

> To learn about basics of the Unified Logging System, take a look at my [
> “Logging in Swift” ](/2022/04/06/logging-in-swift/) post.

Now we can use the identifier to start monitoring an event with a particular
message using the _beginInterval_ function. This function returns a state of
the interval that we will use to associate starting and finishing points of an
event. As the last step, we call the _endInterval_ function by passing a
message and the interval state.

> Remember that the message you use while beginning and ending intervals
> should be the same.

Another thing we might need is attaching metadata to a signpost interval. For
example, we can bind a localized error description whenever interval ends with
an error.

    
    
    func fetchRecent() async {
        let signpostID = Self.signposter.makeSignpostID()
    
        let interval = Self.signposter.beginInterval("Fetching recent", id: signpostID)
        do {
            accountStatus = try await service.checkAccountStatus()
            recentFasting = try await service.fetchAllFastingRecords().last
            Self.signposter.endInterval("Fetching recent", interval)
        } catch {
            Self.signposter.endInterval("Fetching recent", interval, "\(error.localizedDescription, privacy: .public)")
        }
    }
    

We can also emit intermediate events inside a particular interval. It might be
helpful to divide a multi-step event into timepieces to understand which part
of the event is slowing the app.

    
    
    func fetchRecent() async {
        let signpostID = Self.signposter.makeSignpostID()
    
        let interval = Self.signposter.beginInterval("Fetching recent", id: signpostID)
        do {
            accountStatus = try await service.checkAccountStatus()
            Self.signposter.emitEvent("Account status fetched", id: signpostID)
            recentFasting = try await service.fetchAllFastingRecords().last
            Self.signposter.endInterval("Fetching recent", interval)
        } catch {
            Self.signposter.endInterval("Fetching recent", interval, "\(error.localizedDescription, privacy: .public)")
        }
    }
    

In the example above, we use the _emitEvent_ function on the _OSSignposter_
type to emit additional events connected to a particular signpost identifier.

####  Collecting performance data

OK, we learned how to measure app events using the _Signposter_ type. Now it
is time to learn how to read that data to analyze our app performance. There
are two ways of reading the data written by the _Signposter_ type.

First, we can use the Instruments app to visualize all the performance data
nicely. The second is a programmatic way of exporting performance data from
the user devices using the _OSLogStore_ type.

Let’s start with the simplest one. While debugging your app via Xcode, you can
build the app for profiling by pressing CMD + I. In the opened Instruments
app, choose the Logging template. It contains both logs and signposts. Now run
the app by pressing the record button and start interacting and producing
events in your app.

![instruments-logging-template](/public/signpost.png)

Instruments app is a great way to profile your app locally, but sometimes we
need data from the user devices. In this case, we can export the signpost data
using the _OSLogStore_ type.

    
    
    import OSLog
    import Foundation
    
    @MainActor final class LogStore: ObservableObject {
        private static let logger = Logger(
            subsystem: Bundle.main.bundleIdentifier!,
            category: String(describing: LogStore.self)
        )
    
        @Published private(set) var entries: [String] = []
    
        func exportPerformanceData() {
            do {
                let store = try OSLogStore(scope: .currentProcessIdentifier)
                let position = store.position(timeIntervalSinceLatestBoot: 1)
                entries = try store
                    .getEntries(at: position)
                    .compactMap { $0 as? OSLogEntrySignpost }
                    .filter { $0.subsystem == Bundle.main.bundleIdentifier! }
                    .map { "[\($0.date.formatted())] [\($0.category)] [\($0.signpostType)] \($0.signpostName)" }
            } catch {
                Self.logger.warning("\(error.localizedDescription, privacy: .public)")
            }
        }
    }
    

> To learn more about the power of _OSLogStore_ type, take a look at my [
> “Exporting data from Unified Logging System in Swift”
> ](/2022/04/19/exporting-data-from-unified-logging-system-in-swift/) post.

####  Conclusion

Today we learned how to use the Unified Logging System to measure and collect
performance data of our apps. Understanding the performance of particular
events is crucial for building a great user experience. Fortunately, we can
quickly achieve that by using the Unified Logging System. I hope you enjoy the
post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask
your questions related to this post. Thanks for reading, and see you next
week!

