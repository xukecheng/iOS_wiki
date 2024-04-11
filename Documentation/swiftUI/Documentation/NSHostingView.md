Initializer

# init(rootView:)

Creates a hosting view object that wraps the specified SwiftUI view.

macOS 10.15+

    
    
    @MainActor
    required init(rootView: Content)

##  Parameters

`rootView`

    

The root view of the SwiftUI view hierarchy that you want to manage using this
hosting view.

## See Also

### Creating a hosting view

`init?(coder: NSCoder)`

Creates a hosting view object from the contents of the specified archive.

`func prepareForReuse()`

Initializer

# init(coder:)

Creates a hosting view object from the contents of the specified archive.

macOS 10.15+

    
    
    @MainActor
    required dynamic init?(coder aDecoder: NSCoder)

##  Parameters

`coder`

    

The decoder to use during initialization.

## Discussion

The default implementation of this method throws an exception. Use the
`init(rootView:)` method to create your hosting view instead.

## See Also

### Creating a hosting view

`init(rootView: Content)`

Creates a hosting view object that wraps the specified SwiftUI view.

`func prepareForReuse()`

Instance Method

# prepareForReuse()

macOS 10.15+

    
    
    @MainActor
    override dynamic func prepareForReuse()

## See Also

### Creating a hosting view

`init(rootView: Content)`

Creates a hosting view object that wraps the specified SwiftUI view.

`init?(coder: NSCoder)`

Creates a hosting view object from the contents of the specified archive.

Instance Property

# rootView

The root view of the SwiftUI view hierarchy managed by this view controller.

macOS 10.15+

    
    
    @MainActor
    var rootView: Content { get set }

Type Property

# requiresConstraintBasedLayout

macOS 10.15+

    
    
    @MainActor
    override dynamic class var requiresConstraintBasedLayout: Bool { get }

## See Also

### Configuring the view layout behavior

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# userInterfaceLayoutDirection

macOS 10.15+

    
    
    @MainActor
    override dynamic var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# isFlipped

macOS 10.15+

    
    
    @MainActor
    override final var isFlipped: Bool { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# layerContentsRedrawPolicy

macOS 10.15+

    
    
    @MainActor
    override dynamic var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy { get set }

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`func updateConstraints()`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Method

# updateConstraints()

macOS 10.15+

    
    
    @MainActor
    override dynamic func updateConstraints()

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func layout()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Method

# layout()

macOS 10.15+

    
    
    @MainActor
    override dynamic func layout()

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`var safeAreaRegions: SafeAreaRegions`

The safe area regions that this view controller adds to its view.

Instance Property

# safeAreaRegions

The safe area regions that this view controller adds to its view.

macOS 13.3+

    
    
    @MainActor
    var safeAreaRegions: SafeAreaRegions { get set }

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the view layout behavior

`class var requiresConstraintBasedLayout: Bool`

`var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection`

`var isFlipped: Bool`

`var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy`

`func updateConstraints()`

`func layout()`

Instance Method

# keyDown(with:)

Called when the user presses a key on the keyboard while this view is in the
responder chain.

macOS 10.15+

    
    
    @MainActor
    override dynamic func keyDown(with event: NSEvent)

## See Also

### Managing keyboard interaction

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# keyUp(with:)

Called when the user releases a key on the keyboard while this view is in the
responder chain.

macOS 10.15+

    
    
    @MainActor
    override dynamic func keyUp(with event: NSEvent)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# performKeyEquivalent(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func performKeyEquivalent(with event: NSEvent) -> Bool

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func insertText(Any)`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# insertText(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func insertText(_ insertString: Any)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func didChangeValue(forKey: String)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# didChangeValue(forKey:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func didChangeValue(forKey key: String)

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func makeTouchBar() -> NSTouchBar?`

Instance Method

# makeTouchBar()

macOS 10.15+

    
    
    @MainActor
    override dynamic func makeTouchBar() -> NSTouchBar?

## See Also

### Managing keyboard interaction

`func keyDown(with: NSEvent)`

Called when the user presses a key on the keyboard while this view is in the
responder chain.

`func keyUp(with: NSEvent)`

Called when the user releases a key on the keyboard while this view is in the
responder chain.

`func performKeyEquivalent(with: NSEvent) -> Bool`

`func insertText(Any)`

`func didChangeValue(forKey: String)`

Instance Method

# mouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseDown(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseDown(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseUp(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseUp(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseEntered(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseEntered(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseExited(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseExited(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# mouseMoved(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func mouseMoved(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# otherMouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func otherMouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# rightMouseDragged(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rightMouseDragged(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func cursorUpdate(with: NSEvent)`

Instance Method

# cursorUpdate(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func cursorUpdate(with event: NSEvent)

## See Also

### Responding to mouse events

`func mouseDown(with: NSEvent)`

`func mouseUp(with: NSEvent)`

`func otherMouseDown(with: NSEvent)`

`func otherMouseUp(with: NSEvent)`

`func rightMouseDown(with: NSEvent)`

`func rightMouseUp(with: NSEvent)`

`func mouseEntered(with: NSEvent)`

`func mouseExited(with: NSEvent)`

`func mouseDragged(with: NSEvent)`

`func mouseMoved(with: NSEvent)`

`func otherMouseDragged(with: NSEvent)`

`func rightMouseDragged(with: NSEvent)`

Instance Method

# touchesBegan(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesBegan(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesCancelled(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesCancelled(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesCancelled(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesEnded(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesEnded(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesCancelled(with: NSEvent)`

`func touchesMoved(with: NSEvent)`

Instance Method

# touchesMoved(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func touchesMoved(with event: NSEvent)

## See Also

### Responding to touch events

`func touchesBegan(with: NSEvent)`

`func touchesCancelled(with: NSEvent)`

`func touchesEnded(with: NSEvent)`

Instance Method

# magnify(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func magnify(with event: NSEvent)

## See Also

### Responding to gestures

`func rotate(with: NSEvent)`

`func scrollWheel(with: NSEvent)`

Instance Method

# rotate(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func rotate(with event: NSEvent)

## See Also

### Responding to gestures

`func magnify(with: NSEvent)`

`func scrollWheel(with: NSEvent)`

Instance Method

# scrollWheel(with:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func scrollWheel(with event: NSEvent)

## See Also

### Responding to gestures

`func magnify(with: NSEvent)`

`func rotate(with: NSEvent)`

Instance Method

# validRequestor(forSendType:returnType:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func validRequestor(
        forSendType sendType: NSPasteboard.PasteboardType?,
        returnType: NSPasteboard.PasteboardType?
    ) -> Any?

Instance Method

# menu(for:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func menu(for event: NSEvent) -> NSMenu?

Instance Method

# responds(to:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func responds(to selector: Selector!) -> Bool

## See Also

### Responding to actions

`func forwardingTarget(for: Selector!) -> Any?`

`func doCommand(by: Selector)`

Instance Method

# forwardingTarget(for:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func forwardingTarget(for selector: Selector!) -> Any?

## See Also

### Responding to actions

`func responds(to: Selector!) -> Bool`

`func doCommand(by: Selector)`

Instance Method

# doCommand(by:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func doCommand(by selector: Selector)

## See Also

### Responding to actions

`func responds(to: Selector!) -> Bool`

`func forwardingTarget(for: Selector!) -> Any?`

Instance Property

# acceptsFirstResponder

macOS 10.15+

    
    
    @MainActor
    override dynamic var acceptsFirstResponder: Bool { get }

## See Also

### Configuring the responder behavior

`var needsPanelToBecomeKey: Bool`

Instance Property

# needsPanelToBecomeKey

macOS 10.15+

    
    
    @MainActor
    override dynamic var needsPanelToBecomeKey: Bool { get }

## See Also

### Configuring the responder behavior

`var acceptsFirstResponder: Bool`

Instance Method

# viewWillMove(toWindow:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewWillMove(toWindow newWindow: NSWindow?)

## See Also

### Managing the view hierarchy

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidMoveToWindow()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidMoveToWindow()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidChangeBackingProperties()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidChangeBackingProperties()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeEffectiveAppearance()`

`func renewGState()`

Instance Method

# viewDidChangeEffectiveAppearance()

macOS 10.15+

    
    
    @MainActor
    override dynamic func viewDidChangeEffectiveAppearance()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func renewGState()`

Instance Method

# renewGState()

macOS 10.15+

    
    
    @MainActor
    override dynamic func renewGState()

## See Also

### Managing the view hierarchy

`func viewWillMove(toWindow: NSWindow?)`

`func viewDidMoveToWindow()`

`func viewDidChangeBackingProperties()`

`func viewDidChangeEffectiveAppearance()`

Instance Property

# intrinsicContentSize

macOS 10.15+

    
    
    @MainActor
    override dynamic var intrinsicContentSize: NSSize { get }

## See Also

### Modifying the frame rectangle

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Method

# setFrameSize(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func setFrameSize(_ newSize: NSSize)

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# firstBaselineOffsetFromTop

macOS 10.15+

    
    
    @MainActor
    override dynamic var firstBaselineOffsetFromTop: CGFloat { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# lastBaselineOffsetFromBottom

macOS 10.15+

    
    
    @MainActor
    override dynamic var lastBaselineOffsetFromBottom: CGFloat { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

`var firstTextLineCenter: CGFloat?`

Instance Property

# sizingOptions

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

macOS 13.0+

    
    
    @MainActor
    var sizingOptions: NSHostingSizingOptions { get set }

## Discussion

NSHostingView can create minimum, maximum, and ideal (content size)
constraints that are derived from its SwiftUI view content. These constraints
are only created when Auto Layout constraints are otherwise being used in the
containing window.

If the NSHostingView is set as the `contentView` of an `NSWindow`, it will
also update the window’s `contentMinSize` and `contentMaxSize` based on the
minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`,
`intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to
control this behavior. For instance, setting a value of `.minSize` will only
create the constraints necessary to maintain the minimum size of the SwiftUI
content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingView`
relative to its displayed content, such as the always being displayed in a
fixed frame, setting this to a value with fewer options can improve
performance as it reduces the amount of layout measurements that need to be
performed. If an `NSHostingView` has a `frame` that is smaller or larger than
that required to display its SwiftUI content, the content will be centered
within that frame.

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var firstTextLineCenter: CGFloat?`

Instance Property

# firstTextLineCenter

macOS 10.15+

    
    
    @MainActor
    var firstTextLineCenter: CGFloat? { get }

## See Also

### Modifying the frame rectangle

`var intrinsicContentSize: NSSize`

`func setFrameSize(NSSize)`

`var firstBaselineOffsetFromTop: CGFloat`

`var lastBaselineOffsetFromBottom: CGFloat`

`var sizingOptions: NSHostingSizingOptions`

The options for how the hosting view creates and updates constraints based on
the size of its SwiftUI content.

Instance Method

# hitTest(_:)

macOS 10.15+

    
    
    @MainActor
    override dynamic func hitTest(_ point: NSPoint) -> NSView?

Instance Method

# isAccessibilityElement()

macOS 10.15+

    
    
    @MainActor
    override dynamic func isAccessibilityElement() -> Bool

## See Also

### Managing accessibility behaviors

`var accessibilityFocusedUIElement: Any?`

`func accessibilityChildren() -> [Any]?`

`func accessibilityChildrenInNavigationOrder() -> [any
NSAccessibilityElementProtocol]?`

`func accessibilityHitTest(NSPoint) -> Any?`

`func accessibilityRole() -> NSAccessibility.Role?`

`func accessibilitySubrole() -> NSAccessibility.Subrole?`

Instance Property

# sceneBridgingOptions

The options for which aspects of the window will be managed by this hosting
view.

macOS 14.0+

    
    
    @MainActor
    var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }

## Discussion

`NSHostingView` will populate certain aspects of its associated window,
depending on which options are specified.

For example, a hosting view can manage its window’s toolbar by including the
`.toolbars` option:

When this hosting view is set as the `contentView` for a window, the default
value for this property will be `.all`, which includes the options for
`.toolbars` and `.title`. Otherwise, the default value is `[]`.

