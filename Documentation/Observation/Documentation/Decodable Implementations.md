Initializer

# init(from:)

Creates a new instance by decoding from the given decoder.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(from decoder: any Decoder) throws

##  Parameters

`decoder`

    

The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the
data read is corrupted or otherwise invalid.

