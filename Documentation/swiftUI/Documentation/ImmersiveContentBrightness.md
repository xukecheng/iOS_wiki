Type Property

# automatic

The default content brightness.

visionOS 1.0+

    
    
    static let automatic: ImmersiveContentBrightness

Type Property

# bright

A bright content brightness.

visionOS 1.0+

    
    
    static let bright: ImmersiveContentBrightness

Type Property

# dark

A dark content brightness.

visionOS 1.0+

    
    
    static let dark: ImmersiveContentBrightness

Type Property

# dim

A dimmed content brightness.

visionOS 1.0+

    
    
    static let dim: ImmersiveContentBrightness

Type Method

# custom(_:)

Creates a content brightness with a custom value.

visionOS 1.0+

    
    
    static func custom(_ value: Double) -> ImmersiveContentBrightness

##  Parameters

`value`

    

The value of the brightness. Provide a value between 0 and 1. Larger values
correspond to a brighter environment.

