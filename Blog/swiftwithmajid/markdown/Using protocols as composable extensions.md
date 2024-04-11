##  Using protocols as composable extensions

17 Jan 2019

Today we will talk about using protocols as composable pieces for our view
controllers. [ Protocols and Protocol Extensions ](/2019/01/23/maintaining-
state-in-view-controllers) are my second favorite Swift feature after
optionals. It helps us to create highly composable and reusable codebase
without inheritance. For years we were using inheritance as a gold programming
standard. But is it so good? Let’s take a look for simple _BaseViewController_
which we used to have in every project.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

    
    
    import UIKit
    
    class BaseViewController: UIViewController {
        private let activityIndicator = UIActivityIndicatorView(style: .whiteLarge)
    
        override func viewDidLoad() {
            super.viewDidLoad()
            view.addSubview(activityIndicator)
    
            activityIndicator.translatesAutoresizingMaskIntoConstraints = false
            NSLayoutConstraint.activate([
                activityIndicator.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                activityIndicator.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor)
                ])
        }
    
        func presenActivity() {
            activityIndicator.startAnimating()
        }
    
        func dismissActivity() {
            activityIndicator.stopAnimating()
        }
    
        func present(_ error: Error) {
            let alert = UIAlertController(title: error.localizedDescription, message: nil, preferredStyle: .alert)
            alert.addAction(.init(title: "Cancel", style: .cancel))
            present(alert, animated: true)
        }
    }
    

It looks straightforward and usable because most of our view controllers need
activity indicator while downloading data from the internet and error handling
in case of something goes wrong during the data download. But we don’t stop
with this, and we add more features to _BaseViewController_ over a time. It
starts bloating with a lot of general-purpose functions. Here we have at least
two main problems:

  1. Our _BaseViewController_ breaks the Single Responsibility Principle by implementing all these features in one place. Over time it will turn into Massive-View-Controller, which hard to understand and cover with tests. 
  2. Every view controller in our app inherit from _BaseViewController_ to use all these features. In case of a bug in _BaseViewController_ , we will have this bug in all view controllers in our app even if view controller is not using buggy functionality from _BaseViewController_ . 

####  Protocols for the rescue.

Protocol extensions feature was released with Swift 2.0 and bring real power
to protocol types which announce new paradigm of programming: Protocol
Oriented Programming. I recommend you to watch the [ talk
](https://developer.apple.com/videos/play/wwdc2015/408/) from WWDC about
protocols and protocol extensions.

Let’s go back to our topic. How can protocols help us? Let’s start by
declaring _ActivityPresentable_ protocol for presenting and dismissing an
activity indicator.

    
    
    protocol ActivityPresentable {
        func presentActivity()
        func dismissActivity()
    }
    
    extension ActivityPresentable where Self: UIViewController {
        func presentActivity() {
            if let activityIndicator = findActivity() {
                activityIndicator.startAnimating()
            } else {
                let activityIndicator = UIActivityIndicatorView(style: .whiteLarge)
                activityIndicator.startAnimating()
                view.addSubview(activityIndicator)
    
                activityIndicator.translatesAutoresizingMaskIntoConstraints = false
                NSLayoutConstraint.activate([
                    activityIndicator.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                    activityIndicator.centerYAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerYAnchor)
                    ])
            }
        }
    
        func dismissActivity() {
            findActivity()?.stopAnimating()
        }
    
        func findActivity() -> UIActivityIndicatorView? {
            return view.subviews.compactMap { $0 as? UIActivityIndicatorView }.first
        }
    }
    

We extracted _presentActivity_ and _dismissActivity_ methods into the
particular protocol type. We add default implementation via protocol extension
for cases where Type which adopt this protocol is view controller. It gives us
the opportunity of using view controller methods and properties in our
protocol extension.

Let’s do the same for error presenting logic.

    
    
    protocol ErrorPresentable {
        func present(_ error: Error)
    }
    
    extension ErrorPresentable where Self: UIViewController {
        func present(_ error: Error) {
            let alert = UIAlertController(title: error.localizedDescription, message: nil, preferredStyle: .alert)
            alert.addAction(.init(title: "Cancel", style: .cancel))
            present(alert, animated: true)
        }
    }
    

Now we have two reusable protocol types which respect the Single
Responsibility Principle. We can add them as the extension to any view
controller which need this functionality. The nice thing is that we are adding
the only extension which needed in concrete view controller and not inherits
all the stuff from the _BaseViewController_ . Here is the usage example of
these protocols.

    
    
    class ViewController: UIViewController {
        override func viewDidLoad() {
            super.viewDidLoad()
            presentActivity()
        }
    }
    
    extension ViewController: ActivityPresentable, ErrorPresentable {}
    

Another opportunity here is that we can easily ignore default implementation
of the protocol to implement our customized _ActivityIndicator_ for some of
view controllers. Let’s take a look at the example.

    
    
    class CustomViewController: UIViewController {
        override func viewDidLoad() {
            super.viewDidLoad()
            presentActivity()
        }
    }
    
    extension CustomViewController: ActivityPresentable {
        func presentActivity() {
            // Custom activity presenting logic
        }
    
        func dismissActivity() {
    
        }
    }
    

While adopting _CustomViewController_ to _ActivityPresentable_ protocol, we
specify the custom implementation of _presentActivity_ and _dismissActivity_
methods.

####  Conclusion

As you can see, we can use protocols as simple extensions for our view
controller type. In the future posts, we will continue using protocols to
build reusable parts of view controller. We will touch associated type, and
conditional conformance features to develop more generic data based extensions
for view controllers.

Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and ask your
questions related to this post. Thanks for the reading and see you next week.

