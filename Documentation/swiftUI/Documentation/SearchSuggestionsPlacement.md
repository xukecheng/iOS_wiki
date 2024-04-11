Type Property

# automatic

Search suggestions render automatically based on the surrounding context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: SearchSuggestionsPlacement { get }

## Discussion

The behavior varies by platform:

  * In iOS and iPadOS, suggestions render as a list overlaying the main content of the app.

  * In macOS, suggestions render in a menu.

  * In tvOS, suggestions render as a row underneath the search field.

  * In watchOS, suggestions render in a list pushed onto the containing navigation stack.

## See Also

### Getting placements

`static var content: SearchSuggestionsPlacement`

Search suggestions render in the main content of the app.

`static var menu: SearchSuggestionsPlacement`

Search suggestions render inside of a menu attached to the search field.

Type Property

# content

Search suggestions render in the main content of the app.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var content: SearchSuggestionsPlacement { get }

## See Also

### Getting placements

`static var automatic: SearchSuggestionsPlacement`

Search suggestions render automatically based on the surrounding context.

`static var menu: SearchSuggestionsPlacement`

Search suggestions render inside of a menu attached to the search field.

Type Property

# menu

Search suggestions render inside of a menu attached to the search field.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var menu: SearchSuggestionsPlacement { get }

## See Also

### Getting placements

`static var automatic: SearchSuggestionsPlacement`

Search suggestions render automatically based on the surrounding context.

`static var content: SearchSuggestionsPlacement`

Search suggestions render in the main content of the app.

Structure

# SearchSuggestionsPlacement.Set

An efficient set of search suggestion display modes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Set

## Topics

### Getting placement sets

`static var content: SearchSuggestionsPlacement.Set`

A set containing placements with the apps main content, excluding the menu
placement.

`static var menu: SearchSuggestionsPlacement.Set`

A set containing the menu display mode.

### Creating a set

`init(rawValue: Int)`

Creates a set of search suggestions from an integer.

`var rawValue: Int`

The raw value that records the search suggestion display modes.

### Supporting types

`typealias Element`

A type for the elements of the set.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

