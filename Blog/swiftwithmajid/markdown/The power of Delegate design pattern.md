##  The power of Delegate design pattern

29 May 2019

Last week before WWDC and everybody so excited about new features which we
will have just in a few days. However, let’s keep posts related to WWDC for
next week. This week we are going to talk about my favorite design pattern
_Delegate_ . _Delegate_ is the most straightforward and powerful pattern.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In software engineering, the delegation pattern is an object-oriented design
pattern that allows object composition to achieve the same code reuse as an
inheritance. In delegation, an object handles a request by delegating to a
second object (the delegate). A delegate is a helper object, but with the
original context.

####  Protocols

We use _Delegate_ pattern every day, and iOS SDK uses it in many places. For
example, _UITableView_ delegates to _UITableViewDataSource_ populating the
table with cells, it also delegates cell selection and other actions to
_UITableViewDelegate_ . Another excellent example of delegate patters is
_FlowController_ or _Coordinators_ . _ViewControllers_ delegates navigation
logic to _Coordinator_ . I have separated post about [ extracting navigation
logic into FlowControllers ](/2019/02/20/navigation-with-flow-controllers) .

Let’s dive into code samples. Assume that you are working on a game. You
extracted game logic into separated class Game, and you want to delegate game
state changes to _UIViewController_ which renders this game.

    
    
    protocol GameDelegate: AnyObject {
        func stateChanged(from oldState: Game.State, to newState: Game.State)
    }
    
    class Game {
        private var state: State = .notStarted {
            didSet {
                delegate?.stateChanged(from: oldValue, to: state)
            }
        }
    
        weak var delegate: GameDelegate?
    
        private(set) var value: Int = 0
    
        func start() {
            state = .started
        }
    
        func generateNextValue() {
            value = Int.random(in: 0..<1000)
            state = generateState(using: value)
        }
    }
    
    extension Game {
        enum State {
            case notStarted
            case started
            case right
            case win
            case lost
        }
    }
    

Here is the source code of a simple game which generates random values. The
game engine generates state based on random values. Every state change call
delegate to pass old and new states. We define our delegate protocol extended
from _AnyObject_ , that means the only class instance can accept it. I also
use **weak** keyword to define variable holding delegate. It needed to break
the retain cycle between delegate and game class. Let’s take a look at
_GameViewController_ now.

    
    
    class GameViewController: UIViewController {
        private let game: Game
    
        init(game: Game) {
            self.game = game
            super.init(nibName: nil, bundle: nil)
        }
    
        @IBAction func play() {
            game.start()
        }
    
        @IBAction func next() {
            game.generateNextValue()
        }
    
        override func viewDidLoad() {
            super.viewDidLoad()
            game.delegate = self
        }
    }
    
    extension GameViewController: GameDelegate {
        func render(_ state: Game.State) {
            switch state {
            case .lost: renderLost()
            case .right: renderRight()
            case .win: renderWin()
            case .started: renderStart()
            case .notStarted: renderNotStarted()
            }
        }
    
        func stateChanged(from oldState: Game.State, to newState: Game.State) {
            render(newState)
        }
    }
    

Here we have a _GameViewController_ class which feeds game with user actions
and render state changes. _GameViewController_ conforms to _GameDelegate_ and
implements all needed rendering in extension. As a result, we have a
composable codebase with the help of _Delegate_ design pattern.

####  Closures

Sometimes when you have only one method in the delegate, you can replace it
with closure. The idea is the same, but now you call the closure and pass the
state instead of calling the method by protocol. Let’s take a look at the
example with closure.

    
    
    class Game {
        typealias StateHandler = (State) -> Void
    
        var handler: StateHandler?
        
        private var state: State = .notStarted {
            didSet {
                handler?(state)
            }
        }
    }
    
    class GameViewController: UIViewController {
        override func viewDidLoad() {
            super.viewDidLoad()
    
            game.handler = { [weak self] state in
                self?.render(state)
            }
        }
    }
    

As you can see, we pass the closure to the game class instance which handles
state changes. We use **weak** to break the retain cycle during closure’s
context capture. Another option here can be a usage of the fact that any Swift
function is a closure. So instead of creating separated closure, we can pass
the function name. However, be careful this method creates retain circle. Here
is an example of how we can do that.

    
    
    class GameViewController: UIViewController {
        override func viewDidLoad() {
            super.viewDidLoad()
            game.handler = render
        }
    }
    
    extension GameViewController {
        func render(_ state: Game.State) {
            switch state {
            case .lost: renderLost()
            case .right: renderRight()
            case .win: renderWin()
            case .started: renderStart()
            case .notStarted: renderNotStarted()
            }
        }
    }
    

####  Conclusion

Today we discussed the most powerful and straightforward design pattern in iOS
development. I enjoy how simple it is and how useful it can be in composing
pieces to make codebase decoupled. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading and see you next week!

