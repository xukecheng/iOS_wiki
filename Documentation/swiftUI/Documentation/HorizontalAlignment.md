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

