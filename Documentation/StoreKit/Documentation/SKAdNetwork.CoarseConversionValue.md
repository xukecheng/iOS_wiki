Type Property

# high

A string constant value for indicating a high coarse conversion value.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    static let high: SKAdNetwork.CoarseConversionValue

## Discussion

This constant has no special meaning. It’s up to the app or ad network to
determine its meaning as needed.

## See Also

### Providing coarse conversion values

`static let low: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a low coarse conversion value.

`static let medium: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a medium coarse conversion value.

`init(rawValue: String)`

Creates a coarse conversion value from the raw value.

Type Property

# low

A string constant value for indicating a low coarse conversion value.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    static let low: SKAdNetwork.CoarseConversionValue

## Discussion

This constant has no special meaning. It’s up to the app or ad network to
determine its meaning as needed.

## See Also

### Providing coarse conversion values

`static let high: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a high coarse conversion value.

`static let medium: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a medium coarse conversion value.

`init(rawValue: String)`

Creates a coarse conversion value from the raw value.

Type Property

# medium

A string constant value for indicating a medium coarse conversion value.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+

    
    
    static let medium: SKAdNetwork.CoarseConversionValue

## Discussion

This constant has no special meaning. It’s up to the app or ad network to
determine its meaning as needed.

## See Also

### Providing coarse conversion values

`static let high: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a high coarse conversion value.

`static let low: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a low coarse conversion value.

`init(rawValue: String)`

Creates a coarse conversion value from the raw value.

Initializer

# init(rawValue:)

Creates a coarse conversion value from the raw value.

iOS 16.1+  iPadOS 16.1+  Mac Catalyst 16.1+  Xcode 14.0+

    
    
    init(rawValue: String)

##  Parameters

`rawValue`

    

A string that is one of `low`, `medium`, or `high`.

## Discussion

You don't need to call the initializer to use coarse conversion values. When
you provide the coarse conversion value to the
`updatePostbackConversionValue(_:coarseValue:completionHandler:)` or
`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`
methods, use the static constants, `low`, `medium`, or `high`.

## See Also

### Providing coarse conversion values

`static let high: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a high coarse conversion value.

`static let low: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a low coarse conversion value.

`static let medium: SKAdNetwork.CoarseConversionValue`

A string constant value for indicating a medium coarse conversion value.

