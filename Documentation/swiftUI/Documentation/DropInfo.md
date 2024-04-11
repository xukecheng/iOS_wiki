Instance Property

# location

The location of the drag in the coordinate space of the drop view.

iOS 13.4+  iPadOS 13.4+  macOS 10.15+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    var location: CGPoint { get }

Instance Method

# hasItemsConforming(to:)

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func hasItemsConforming(to contentTypes: [UTType]) -> Bool

##  Parameters

`contentTypes`

    

The uniform type identifiers to query for.

## Return Value

Whether at least one item conforms to one of `contentTypes`.

## See Also

### Checking for items

`func itemProviders(for: [UTType]) -> [NSItemProvider]`

Finds item providers that conform to at least one of the specified uniform
type identifiers.

Instance Method

# itemProviders(for:)

Finds item providers that conform to at least one of the specified uniform
type identifiers.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    func itemProviders(for contentTypes: [UTType]) -> [NSItemProvider]

##  Parameters

`contentTypes`

    

The uniform type identifiers to query for.

## Return Value

The item providers that conforms to `contentTypes`.

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Checking for items

`func hasItemsConforming(to: [UTType]) -> Bool`

Indicates whether at least one item conforms to at least one of the specified
uniform type identifiers.

Instance Method

# hasItemsConforming(to:)

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func hasItemsConforming(to types: [String]) -> Bool

Deprecated

Use `hasItemsConforming(to:)` instead.

## See Also

### Deprecated symbols

`func itemProviders(for: [String]) -> [NSItemProvider]`

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

Deprecated

Instance Method

# itemProviders(for:)

Returns an array of items that each conform to at least one of the specified
uniform type identifiers.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  visionOS 1.0+

    
    
    func itemProviders(for types: [String]) -> [NSItemProvider]

Deprecated

Use `itemProviders(for:)` instead.

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Deprecated symbols

`func hasItemsConforming(to: [String]) -> Bool`

Returns whether at least one item conforms to at least one of the specified
uniform type identifiers.

Deprecated

