Type Property

# intrinsicContentSize

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

macOS 13.0+

    
    
    static let intrinsicContentSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

## See Also

### Geting sizing options

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# maxSize

The hosting view creates and updates constraints that represent its content’s
maximum size.

macOS 13.0+

    
    
    static let maxSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `width: infinity,
height: infinity`.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# minSize

The hosting view creates and updates constraints that represent its content’s
minimum size.

macOS 13.0+

    
    
    static let minSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `width: 0, height:
0`.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# preferredContentSize

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

macOS 13.0+

    
    
    static let preferredContentSize: NSHostingSizingOptions

## Discussion

The constraints reflect the size that fits a proposal of `.unspecified`.

Note

this option has no effect when used with an `NSHostingView` directly.

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let standardBounds: NSHostingSizingOptions`

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

Type Property

# standardBounds

The hosting view creates constraints for its minimum, ideal, and maximum
sizes.

macOS 13.0+

    
    
    static let standardBounds: NSHostingSizingOptions

## See Also

### Geting sizing options

`static let intrinsicContentSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
ideal size. These constraints in turn influence the hosting view’s
`intrinsicContentSize`.

`static let maxSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
maximum size.

`static let minSize: NSHostingSizingOptions`

The hosting view creates and updates constraints that represent its content’s
minimum size.

`static let preferredContentSize: NSHostingSizingOptions`

The hosting controller creates and updates constraints that represent its
content’s ideal size. These constraints in turn influence the hosting
controller’s `preferredContentSize`.

Initializer

# init(rawValue:)

Creates a new options from a raw value.

macOS 13.0+

    
    
    init(rawValue: Int)

## See Also

### Creating a sizing option

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

macOS 13.0+

    
    
    let rawValue: Int

## See Also

### Creating a sizing option

`init(rawValue: Int)`

Creates a new options from a raw value.

