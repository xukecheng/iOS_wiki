Type Property

# all

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

macOS 14.0+

    
    
    static let all: NSHostingSceneBridgingOptions

## See Also

### Geting bridging options

`static let title: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

`static let toolbars: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

Type Property

# title

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

macOS 14.0+

    
    
    static let title: NSHostingSceneBridgingOptions

## Discussion

Title bars populated in this manner overwrite any values set using AppKit.

## See Also

### Geting bridging options

`static let all: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

`static let toolbars: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

Type Property

# toolbars

The hosting view’s associated window will have its toolbar populated with any
items provided to the `toolbar(content:)` modifier.

macOS 14.0+

    
    
    static let toolbars: NSHostingSceneBridgingOptions

## Discussion

Toolbars populated in this manner overwrite any toolbar set on the window
using AppKit.

## See Also

### Geting bridging options

`static let all: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have both its title bars and
toolbars populated with values from their respective modifiers.

`static let title: NSHostingSceneBridgingOptions`

The hosting view’s associated window will have its title and subtitle
populated with the values provided to the `navigationTitle(_:)` and
`navigationSubtitle(_:)` modifiers, respectively.

Initializer

# init(rawValue:)

Creates a new set from a raw value.

macOS 14.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value with which to create the hosting window options.

## See Also

### Creating a bridging options

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

macOS 14.0+

    
    
    let rawValue: Int

## See Also

### Creating a bridging options

`init(rawValue: Int)`

Creates a new set from a raw value.

