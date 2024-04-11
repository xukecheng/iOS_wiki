Type Property

# top

A guide that marks the top edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let top: VerticalAlignment

## Discussion

Use this guide to align the top edges of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# center

A guide that marks the vertical center of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let center: VerticalAlignment

## Discussion

Use this guide to align the centers of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# bottom

A guide that marks the bottom edge of the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let bottom: VerticalAlignment

## Discussion

Use this guide to align the bottom edges of views:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# firstTextBaseline

A guide that marks the top-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let firstTextBaseline: VerticalAlignment

## Discussion

Use this guide to align with the baseline of the top-most text in a view. The
guide aligns with the bottom of a view that contains no text:

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

Type Property

# lastTextBaseline

A guide that marks the bottom-most text baseline in a view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let lastTextBaseline: VerticalAlignment

## Discussion

Use this guide to align with the baseline of the bottom-most text in a view.
The guide aligns with the bottom of a view that contains no text.

The following code generates the image above using an `HStack`:

## See Also

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

Initializer

# init(_:)

Creates a custom vertical alignment of the specified type.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ id: any AlignmentID.Type)

##  Parameters

`id`

    

The type of an identifier that uniquely identifies a vertical alignment.

## Discussion

Use this initializer to create a custom vertical alignment. Define an
`AlignmentID` type, and then use that type to create a new static property on
`VerticalAlignment`:

Every vertical alignment instance that you create needs a unique identifier.
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

For most alignment types, this method returns the mean of all non-`nil`
values. However, some types use other rules. For example, `firstTextBaseline`
returns the minimum value, while `lastTextBaseline` returns the maximum value.

## See Also

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom vertical alignment of the specified type.

