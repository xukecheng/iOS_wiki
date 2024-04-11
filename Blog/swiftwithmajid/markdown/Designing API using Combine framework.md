##  Designing API using Combine framework

07 Apr 2021

Combine framework provides a declarative Swift API for processing values over
time. It allows you to chain, transform and reduce multiple operations. This
week we will learn how to design our APIs using the Combine framework to
leverage all the data processing power that the framework provides us.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Future and Deferred publishers

The easiest way to integrate your asynchronous API with the Combine framework
is to use _Future_ publisher. All you need to do is provide closure that calls
the completion handler whenever it finishes the job. Let’s take a look at the
simple example.

    
    
    final class HealthService {
        private let store = HKHealthStore()
    
        func authorize() -> AnyPublisher<Bool, Error> {
            Future { handler in
                self.store.requestAuthorization(
                    toShare: [.workout], 
                    read: [.hr]
                ) { success, error in
                    if let error = error {
                        handler(.failure(error))
                    } else {
                        handler(.success(success))
                    }
                }
            }.eraseToAnyPublisher()
        }
    

As you can see in the example above, we wrap the old school HealthKit API with
_Future_ publisher. Inside the _Future_ publisher, we call the asynchronous
method of _HKHealthStore_ to authorize the user. We deliver the result of the
_HKHealthStore_ ’s authorize method using the handler of _Future_ publisher.

The _Future_ publisher has a few downsides, and one of them is the publisher’s
eager nature. It means Combine will run the publisher as soon as you create
it.

    
    
    let health = HealthService()
    let authPublisher = health.authorize()
    

In the example above, we create an instance of an authorization publisher but
never subscribe to it. We expect that Combine will run the publisher later
when we subscribe to it using a _sink_ or _assign_ , but it runs immediately.
The Combine framework provides us the _Deferred_ publisher that prevents these
situations.

    
    
    final class HealthService {
        private let store = HKHealthStore()
    
        func authorize() -> AnyPublisher<Bool, Error> {
            Deferred {
                Future { handler in
                    self.store.requestAuthorization(
                        toShare: [.workout], 
                        read: [.hr]
                    ) { success, error in
                        if let error = error {
                            handler(.failure(error))
                        } else {
                            handler(.success(success))
                        }
                    }
                }
            }.eraseToAnyPublisher()
        }
    }
    

We can quickly wrap a _Future_ publisher with a _Deferred_ publisher to make
it lazy. _Deferred_ publisher runs only when we subscribe to it. Now we can
use our new API and leverage all the power of declarative value processing.

    
    
    let health = HealthService()
    var cancellables: Set<AnyCancellable> = []
    
    health
        .authorize()
        .retry(3)
        .replaceError(with: false)
        .sink { print("user authorized: \($0)") }
        .store(in: &cancellables)
    

> To learn more about the set of operators that the Combine framework provides
> us, take a look at my [ “Catching errors in Combine” ](/2020/04/22/catching-
> errors-in-combine/) post.

####  PassthroughSubject

_Future_ publisher works excellent when you need to wrap the asynchronous task
and deliver a single result. But what about the stream of values that we want
to provide over time? We can’t do that with _Future_ publisher because it
finishes its work as soon as it delivers the first result. We can handle this
case with _PassthroughSubject_ .

_PassthroughSubject_ is a publisher that you can use to inject values into a
stream by calling its _send_ method. We will use _PassthroughSubject_ to
design the APIs that provide values through time. For example, it might be
user location or user heart rate. These values appear over time.

    
    
    final class HealthService1 {
        private let store = HKHealthStore()
    
        func heartRate() -> AnyPublisher<[Double], Error> {
            let subject = PassthroughSubject<[Double], Error>()
    
            let query = HKAnchoredObjectQuery(
                type: HKQuantityType.heartRate,
                predicate: nil,
                anchor: nil,
                limit: HKObjectQueryNoLimit
            ) { query, newSamples, _, _, error in
                if let error = error {
                    subject.send(completion: .failure(error))
                } else {
                    let newSamples = newSamples as? [HKQuantitySample] ?? []
                    let hr = newSamples.compactMap { $0.quantity.doubleValue(for: .bpm()) }
                    subject.send(hr)
                }
            }
    
            return subject.handleEvents(
                receiveSubscription: { _ in self.store.execute(query) },
                receiveCancel: { self.store.stop(query) }
            ).eraseToAnyPublisher()
        }
    }
    

As you can see, we use the subject’s _send_ method to emit values that we
obtain from a closure-based handler of _HKAnchoredObjectQuery_ .
_HKAnchoredObjectQuery_ runs forever. That’s why we use the _handleEvents_
operator to provide additional logic to handle the publisher’s lifecycle. We
want to start the query only when we have a subscription and stop it
immediately when the subscription is canceled.

    
    
    var cancellables: Set<AnyCancellable> = []
    
    health
        .authorize()
        .retry(3)
        .flatMap { authorized -> AnyPublisher<[Double], Error> in
            if authorized {
                return health.heartRate().eraseToAnyPublisher()
            } else {
                return Empty().eraseToAnyPublisher()
            }
        }
        .replaceError(with: [])
        .sink { print("user authorized: \($0)") }
        .store(in: &cancellables)
    

####  Conclusion

Combine provides us a straightforward and friendly way to handle asynchronous
operations. We need to design our own APIs using the Combine to leverage the
powerful operators that it gives us. We can model complex operation chains
using a declarative approach and tools like _Future_ and _PassthroughSubject_
. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

