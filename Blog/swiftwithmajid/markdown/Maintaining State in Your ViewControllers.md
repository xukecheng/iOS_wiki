##  Maintaining State in Your ViewControllers

23 Jan 2019

Last week we talked about [ extracting reusable code samples from view
controllers into protocols and protocol extensions ](/2019/01/17/using-
protocols-as-composable-extensions/) . Today I want to show you another nice
use case of protocols while maintaining the state of view controllers.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Assume that we have a screen for presenting the list of user watched shows —
our app downloads it from the web service like Trakt. We can describe the
state of view controller within three variables:

    
    
    class HistoryViewController: UIViewController {
        var loading: Bool = false {
            didSet {
                renderLoading()
            }
        }
    
        var shows: [Show]? {
            didSet {
                renderShows()
            }
        }
    
        var error: Error? {
            didSet {
                renderError()
            }
        }
    }
    

  1. loading indicates whether the view controller loading the data or already finished the job. 
  2. shows variable stores the actual history of watched TV shows. 
  3. error property reports whether the request ended with an error. 

Here is fetch method, which used to request data from Trakt web service:

    
    
        private func fetch() {
            loading = true
            historyService.fetch { [weak self] result in
                self?.loading = false
                switch result {
                case .success(let shows): self?.shows = shows
                case .failure(let error): self?.error = error
                }
            }
        }
    

Before starting our request to Trakt web service, we set loading to true,
which calls _renderLoading_ method. After that, we initiate the API request to
fetch the history of watched TV shows. In the completion handler, we set shows
or error variables accordingly to the result of the request. At first glance,
it should work pretty well, but here we have a couple of downsides.

  1. We have to reset loading, error, shows variables on every request to avoid an invalid state. For example, in case of the first request fails and user retries it with the successful request, we still have value in the error property. 
  2. We want an exclusive state, at any point, we need only one state of the screen: error or loading or shows. Right now we introduce more state variations than we have, and this can leads to ambiguous situations. 

####  Enums

We want the exclusive state, and this is about enums. Enums give the
opportunity to have only one case at any point in time. Let’s refactor our
code with enum.

    
    
    enum State {
        case loading
        case error(Error)
        case loaded([Show])
    }
    
    class HistoryViewController: UIViewController {
        private var state: State {
            didSet {
                render()
            }
        }
    }
    
    extension HistoryViewController {
        func render() {
            switch state {
            case .loading: // render loading
            case .error(let error): // render error
            case loaded(let shows): // render shows
            }
        }
    }
    

Here we declare _State_ enum which exclusively describes our state cases. As
soon as state variable changes, it calls the _render_ method. Inside the
_render_ method, we switch state to display it. Another positive change here
is clean access to screen state. We don’t need to check all the three
variables to understand what’s happening on the screen right now.

####  Protocols with associated types

We already made nice refactoring, but it is very bounded to current screen,
which presents the list of the shows. Let’s add a generic constraint to
_State_ enum, to make it more usable across the app screens, which also have
loading and error states, but present other data entities.

    
    
    enum State<Data> {
        case loading
        case loaded(Data)
        case error(Error)
    }
    

Let’s go beyond and extract state handling into a generic protocol with
protocol extension, which any view controller can adapt to add this logic.

    
    
    protocol StatePresentable: ActivityPresentable, ErrorPresentable {
        associatedtype Data
    
        var state: State<Data> { get set }
        func render()
        func render(_ data: Data)
    }
    
    extension StatePresentable {
        func render() {
            switch state {
            case .loading:
                setActivityStatus(.visible)
            case .error(let error):
                setActivityStatus(.hidden)
                present(error)
            case .loaded(let data):
                setActivityStatus(.hidden)
                render(data)
            }
        }
    }
    

Here we have _StatePresentable_ protocol which extends from
_ActivityPresentable_ and _ErrorPresentable_ protocols. We described these two
protocols in the previous [ post ](/2019/01/17/using-protocols-as-composable-
extensions/) . _StatePresentable_ protocol has associated type Data, which we
use as generic constraint for _State_ enum, to make it usable for any type of
data. We also added the default implementation for _render_ method which
handles state changes.

Here is the usage example of _StatePresentable_ protocol.

    
    
    class HistoryViewController: UIViewController {
        private var state: State<[Show]> {
            didSet {
                render()
            }
        }
    }
    
    extension HistoryViewController: StatePresentable {
        func render(_ data: [Show]) {
            // render your data here
        }
    }
    

All we need is to conform _StatePresentable_ protocol, add the _didSet_
observer for state property and implement _render_ method, where we add data
presenting logic for the actual screen.

####  Conclusion

Protocol with associated types can be robust by enabling the power of generic
constraints and making codebase more reusable. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading and see you next week!

