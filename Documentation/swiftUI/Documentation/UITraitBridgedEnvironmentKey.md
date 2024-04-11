Type Method

# read(from:)

Reads the trait value from the trait collection, and returns the equivalent
environment value.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static func read(from traitCollection: UITraitCollection) -> Self.Value

**Required**

##  Parameters

`traitCollection`

    

The trait collection to read from.

## See Also

### Managing the keys

`static func write(to: inout any UIMutableTraits, value: Self.Value)`

**Required**

Type Method

# write(to:value:)

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS 1.0+

    
    
    static func write(
        to mutableTraits: inout any UIMutableTraits,
        value: Self.Value
    )

**Required**

## See Also

### Managing the keys

`static func read(from: UITraitCollection) -> Self.Value`

Reads the trait value from the trait collection, and returns the equivalent
environment value.

**Required**

