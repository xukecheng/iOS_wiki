##  Building ViewModels with Combine framework

05 Feb 2020

One of my first posts on this blog was about using the ViewModel pattern in
iOS apps. I’m still using this concept in some old school UIKit projects. But
I think it’s time to remaster that post. This week we will talk about building
reactive ViewModels using Combine framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  What is ViewModel?

ViewModel is a layer between your view and data. ViewModels usually fetch the
data using service objects, format it, and provide a formatted version to your
view.

> You can check [ my old post about MVVM ](/2018/01/11/mastering-mvvm-on-ios/)
> if you need more information about the pattern itself.

####  Apple started promoting MVVM

I noticed an interesting thing when Apple moved the _ObservableObject_
protocol to the Combine framework. It looks like Apple began promoting the
MVVM pattern. Let’s take a look at the _ObservableObject_ protocol to
understand what’s going on there.

    
    
    /// A type of object with a publisher that emits before the object has changed.
    public protocol ObservableObject : AnyObject {
    
        /// The type of publisher that emits before the object has changed.
        associatedtype ObjectWillChangePublisher : Publisher = ObservableObjectPublisher where Self.ObjectWillChangePublisher.Failure == Never
    
        /// A publisher that emits before the object has changed.
        var objectWillChange: Self.ObjectWillChangePublisher { get }
    }
    

_ObservableObject_ protocol has the only one requirement, a publisher that
emits before the object changes. Let’s write our first ViewModel that conforms
to _ObservableObject_ protocol.

    
    
    final class PostsViewModel: ObservableObject {
        let objectWillChange = PassthroughSubject<Void, Never>()
    
        private (set) var posts: [Post] = []
    
        func fetch() {
            // fetch posts
            objectWillChange.send()
            // assign new data to the posts variable
        }
    }
    

Here we have the ViewModel that fetches posts, stores them in the variable,
and emits a notification via _objectWillChange_ publisher. Let’s take a look
at a sample _ViewController_ that uses this ViewModel.

    
    
    final class PostsViewController: UIViewController {
        let viewModel: PostsViewModel
        private var cancellables: Set<AnyCancellable> = []
    
        override func viewDidLoad() {
            super.viewDidLoad()
            bindViewModel()
            viewModel.fetch()
        }
    
        private func bindViewModel() {
            viewModel.objectWillChange.sink { [weak self] in
                guard let self = self else {
                    return
                }
                self.renderPosts(self.viewModel.posts)
            }.store(in: &cancellables)
        }
    }
    

As you can see in the example above, we have _PostsViewController_ that starts
observing changes in ViewModel and then ask ViewModel to fetch data. As soon
as ViewModel fetches data, it emits, and _ViewController_ calls renderPosts
function that displays downloaded posts.

####  Published property wrapper

We can go further by using @ _Published_ property wrapper. @ _Published_
property wrapper allows us to wrap any property with the publisher that emits
the current value whenever the property changes.

Moreover, you even don’t need to define _objectWillChange_ publisher when you
use @ _Published_ property wrapper. Swift compiler will **automatically
synthesize** the _objectWillChange_ , and it will emit whenever any @
_Published_ property changes. Let’s take a look at the refactored version of
our ViewModel that uses @ _Published_ property wrapper.

    
    
    final class PostsViewModel: ObservableObject {
        @Published private(set) var posts: [Post] = []
    
        func fetch() {
            // fetch posts and assign them to `posts` variable
        }
    }
    

As you can see in the example above, we don’t need to send a value manually to
_objectWillChange_ publisher — all the work synthesized by the Swift compiler.
And we can keep the same implementation of _PostsViewController_ .

As I said before, @ _Published_ property wrapper wraps our property with a
publisher. Let’s take a look at how we can use it in our _PostsViewController_
.

    
    
    final class PostsViewController: UIViewController {
        let viewModel: PostsViewModel
        private var cancellables: Set<AnyCancellable> = []
    
        override func viewDidLoad() {
            super.viewDidLoad()
            bindViewModel()
            viewModel.fetch()
        }
    
        private func bindViewModel() {
            viewModel.$posts
                .sink { [weak self] in self?.renderPosts($0) }
                .store(in: &cancellables)
        }
    }
    

Here we have a refactored version of our _PostsViewController_ . Please take a
look at how we changed _bindViewModel_ function. It subscribes to _$posts_
now, and it allows us to update our view only when specific properties change.
You will see the benefits as soon as your ViewModel has more and more fields
which can affect the view.

> Apple also mentioned ViewModels during [ “Mastering Xcode Previews” session
> on WWDC 19 ](https://developer.apple.com/wwdc19/233) .

####  Conclusion

We can easily implement the very same logic using _RxSwift_ , _ReactiveSwift_
, or any other reactive framework like _Bond_ . But I feel like _MVVM_ is
going to be a default choice in architecting iOS apps. At least now, when
Apple provides us all the needed tools to build it out of the box. I hope you
enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

