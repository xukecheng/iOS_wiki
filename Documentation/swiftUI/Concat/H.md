# HoverPhase

Case

# HoverPhase.active(_:)

The pointer’s location moved to the specified point within the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    case active(CGPoint)

## See Also

### Getting hover phases

`case ended`

The pointer exited the view.

Case

# HoverPhase.ended

The pointer exited the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    case ended

## See Also

### Getting hover phases

`case active(CGPoint)`

The pointer’s location moved to the specified point within the view.



# HierarchicalShapeStyle

Type Property

# primary

A shape style that maps to the first level of the current content style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let primary: HierarchicalShapeStyle

## See Also

### Getting hierarchical shape styles

`static let secondary: HierarchicalShapeStyle`

A shape style that maps to the second level of the current content style.

`static let tertiary: HierarchicalShapeStyle`

A shape style that maps to the third level of the current content style.

`static let quaternary: HierarchicalShapeStyle`

A shape style that maps to the fourth level of the current content style.

Type Property

# secondary

A shape style that maps to the second level of the current content style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let secondary: HierarchicalShapeStyle

## See Also

### Getting hierarchical shape styles

`static let primary: HierarchicalShapeStyle`

A shape style that maps to the first level of the current content style.

`static let tertiary: HierarchicalShapeStyle`

A shape style that maps to the third level of the current content style.

`static let quaternary: HierarchicalShapeStyle`

A shape style that maps to the fourth level of the current content style.

Type Property

# tertiary

A shape style that maps to the third level of the current content style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let tertiary: HierarchicalShapeStyle

## See Also

### Getting hierarchical shape styles

`static let primary: HierarchicalShapeStyle`

A shape style that maps to the first level of the current content style.

`static let secondary: HierarchicalShapeStyle`

A shape style that maps to the second level of the current content style.

`static let quaternary: HierarchicalShapeStyle`

A shape style that maps to the fourth level of the current content style.

Type Property

# quaternary

A shape style that maps to the fourth level of the current content style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let quaternary: HierarchicalShapeStyle

## See Also

### Getting hierarchical shape styles

`static let primary: HierarchicalShapeStyle`

A shape style that maps to the first level of the current content style.

`static let secondary: HierarchicalShapeStyle`

A shape style that maps to the second level of the current content style.

`static let tertiary: HierarchicalShapeStyle`

A shape style that maps to the third level of the current content style.

Type Property

# quinary

A shape style that maps to the fifth level of the current content style.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let quinary: HierarchicalShapeStyle



# HorizontalEdge

Case

# HorizontalEdge.leading

The leading edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case leading

## See Also

### Getting the edges

`case trailing`

The trailing edge.

Case

# HorizontalEdge.trailing

The trailing edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    case trailing

## See Also

### Getting the edges

`case leading`

The leading edge.

Structure

# HorizontalEdge.Set

An efficient set of horizontal edges.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    struct Set

## Topics

### Getting edge sets

`static let all: HorizontalEdge.Set`

A set containing the leading and trailing horizontal edges.

`static let leading: HorizontalEdge.Set`

A set containing only the leading horizontal edge.

`static let trailing: HorizontalEdge.Set`

A set containing only the trailing horizontal edge.

### Creating an edge set

`init(HorizontalEdge)`

Creates a set of edges containing only the specified horizontal edge.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`



# HorizontalEdge.Set

Type Property

# all

A set containing the leading and trailing horizontal edges.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let all: HorizontalEdge.Set

## See Also

### Getting edge sets

`static let leading: HorizontalEdge.Set`

A set containing only the leading horizontal edge.

`static let trailing: HorizontalEdge.Set`

A set containing only the trailing horizontal edge.

Type Property

# leading

A set containing only the leading horizontal edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let leading: HorizontalEdge.Set

## See Also

### Getting edge sets

`static let all: HorizontalEdge.Set`

A set containing the leading and trailing horizontal edges.

`static let trailing: HorizontalEdge.Set`

A set containing only the trailing horizontal edge.

Type Property

# trailing

A set containing only the trailing horizontal edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let trailing: HorizontalEdge.Set

## See Also

### Getting edge sets

`static let all: HorizontalEdge.Set`

A set containing the leading and trailing horizontal edges.

`static let leading: HorizontalEdge.Set`

A set containing only the leading horizontal edge.

Initializer

# init(_:)

Creates a set of edges containing only the specified horizontal edge.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ edge: HorizontalEdge)



# HSplitView

Initializer

# init(content:)

macOS 10.15+

    
    
    init(@ViewBuilder content: () -> Content)



# HandActivationBehavior

Type Property

# automatic

The default activation behavior, including direct touch, direct pinch, and
indirect pinch.

visionOS 1.0+

    
    
    static let automatic: HandActivationBehavior

## See Also

### Getting the behaviors

`static let pinch: HandActivationBehavior`

Activation that requires a pinched hand.

Type Property

# pinch

Activation that requires a pinched hand.

visionOS 1.0+

    
    
    static let pinch: HandActivationBehavior

## See Also

### Getting the behaviors

`static let automatic: HandActivationBehavior`

The default activation behavior, including direct touch, direct pinch, and
indirect pinch.



# HelpLink

Initializer

# init(action:)

Constructs a new help link with the specified action.

macOS 14.0+  visionOS 1.0+

    
    
    init(action: @escaping () -> Void)

##  Parameters

`action`

    

the action to perform when the user clicks the button.

## Discussion

Use this initializer when you want the standard help button appearance with a
custom button action that does not open an article in an Apple Help book.

## See Also

### Creating a help link

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(destination:)

Constructs a new help link that opens the specified destination URL.

macOS 14.0+  visionOS 1.0+

    
    
    init(destination: URL)

##  Parameters

`destination`

    

The URL to open when the button is clicked.

## Discussion

Use this initializer when you want the standard help button appearance that
opens a link to a website.

You can override the default behavior when the button is clicked by setting
the `openURL` environment value with a custom `OpenURLAction`.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(anchor:)

Constructs a new help link with the specified anchor in the main app bundle’s
book.

macOS 14.0+  visionOS 1.0+

    
    
    init(anchor: NSHelpManager.AnchorName)

##  Parameters

`anchor`

    

The anchor within the help book to open to.

## Discussion

The main app bundle book name is defined by the `CFBundleHelpBookName` key in
its Info.plist file.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName, book: NSHelpManager.BookName)`

Constructs a new help link with the specified anchor and book.

Initializer

# init(anchor:book:)

Constructs a new help link with the specified anchor and book.

macOS 14.0+  visionOS 1.0+

    
    
    init(
        anchor: NSHelpManager.AnchorName,
        book: NSHelpManager.BookName
    )

##  Parameters

`anchor`

    

The anchor within the help book to open to.

`book`

    

The specific book name to open.

## See Also

### Creating a help link

`init(action: () -> Void)`

Constructs a new help link with the specified action.

`init(destination: URL)`

Constructs a new help link that opens the specified destination URL.

`init(anchor: NSHelpManager.AnchorName)`

Constructs a new help link with the specified anchor in the main app bundle’s
book.



# HiddenTitleBarWindowStyle

Initializer

# init()

Creates a hidden title bar window style.

macOS 11.0+

    
    
    init()



# HoverEffect

Type Property

# automatic

An effect that attempts to determine the effect automatically. This is the
default effect.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    static let automatic: HoverEffect

## See Also

### Getting hover effects

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

Type Property

# highlight

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 17.0+  visionOS 1.0+

    
    
    static let highlight: HoverEffect

## Discussion

On tvOS, it applies a projection effect accompanied with a specular highlight
on the view when contained within a focused view. It also incorporates motion
effects to produce a parallax effect by adjusting the projection matrix and
specular offset.

## See Also

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let lift: HoverEffect`

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

Type Property

# lift

An effect that slides the pointer under the view and disappears as the view
scales up and gains a shadow.

iOS 13.4+  iPadOS 13.4+  Mac Catalyst 13.4+  tvOS 16.0+  visionOS 1.0+

    
    
    static let lift: HoverEffect

## See Also

### Getting hover effects

`static let automatic: HoverEffect`

An effect that attempts to determine the effect automatically. This is the
default effect.

`static let highlight: HoverEffect`

An effect that morphs the pointer into a platter behind the view and shows a
light source indicating position.



# HorizontalAlignment

Type Property

# leading

A guide that marks the leading edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let leading: HorizontalAlignment

## Discussion

Use this guide to align the leading edges of views. For a device that uses a
left-to-right language, the leading edge is on the left:

The following code generates the image above using a `VStack`:

## See Also

### Getting guides

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

Type Property

# center

A guide that marks the horizontal center of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let center: HorizontalAlignment

## Discussion

Use this guide to align the centers of views:

The following code generates the image above using a `VStack`:

## See Also

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

Type Property

# trailing

A guide that marks the trailing edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let trailing: HorizontalAlignment

## Discussion

Use this guide to align the trailing edges of views. For a device that uses a
left-to-right language, the trailing edge is on the right:

The following code generates the image above using a `VStack`:

## See Also

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

Type Property

# listRowSeparatorLeading

A guide marking the leading edge of a `List` row separator.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static let listRowSeparatorLeading: HorizontalAlignment

## Discussion

Use this guide to align the leading end of the bottom `List` row separator
with any other horizontal guide of a view that is part of the cell content.

The following example shows the row separator aligned with the leading edge of
the `Text` containing the name of food:

To change the visibility or tint of the row separator use respectively
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`.

## See Also

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

Type Property

# listRowSeparatorTrailing

A guide marking the trailing edge of a `List` row separator.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    static let listRowSeparatorTrailing: HorizontalAlignment

## Discussion

Use this guide to align the trailing end of the bottom `List` row separator
with any other horizontal guide of a view that is part of the cell content.

To change the visibility or tint of the row separator use respectively
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`.

## See Also

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

Initializer

# init(_:)

Creates a custom horizontal alignment of the specified type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ id: any AlignmentID.Type)

##  Parameters

`id`

    

The type of an identifier that uniquely identifies a horizontal alignment.

## Discussion

Use this initializer to create a custom horizontal alignment. Define an
`AlignmentID` type, and then use that type to create a new static property on
`HorizontalAlignment`:

Every horizontal alignment instance that you create needs a unique identifier.
For more information, see `AlignmentID`.

## See Also

### Creating a custom alignment

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

Instance Method

# combineExplicit(_:)

Merges a sequence of explicit alignment values produced by this instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func combineExplicit<S>(_ values: S) -> CGFloat? where S : Sequence, S.Element == CGFloat?

## Discussion

For built-in horizontal alignment types, this method returns the mean of all
non-`nil` values.

## See Also

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom horizontal alignment of the specified type.



# HStack

Initializer

# init(alignment:spacing:content:)

Creates a horizontal stack with the given spacing and vertical alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. This guide has the same
vertical screen coordinate for every subview.

`spacing`

    

The distance between adjacent subviews, or `nil` if you want the stack to
choose a default distance for each pair of subviews.

`content`

    

A view builder that creates the content of this stack.



# HStackLayout

Initializer

# init(alignment:spacing:)

Creates a horizontal stack with the specified spacing and vertical alignment.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. It has the same vertical
screen coordinate for all subviews.

`spacing`

    

The distance between adjacent subviews. Set this value to `nil` to use default
distances between subviews.

Instance Property

# alignment

The vertical alignment of subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var alignment: VerticalAlignment

## See Also

### Getting the stack’s properties

`var spacing: CGFloat?`

The distance between adjacent subviews.

Instance Property

# spacing

The distance between adjacent subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var spacing: CGFloat?

## Discussion

Set this value to `nil` to use default distances between subviews.

## See Also

### Getting the stack’s properties

`var alignment: VerticalAlignment`

The vertical alignment of subviews.



