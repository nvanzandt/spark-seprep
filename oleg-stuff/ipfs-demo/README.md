### IPFS Demo

If we have time for this demo, this is how it will work.

### Installing IPFS

Students can download either [IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop)
or [IPFS CLI](https://docs.ipfs.tech/install/command-line/#install-official-binary-distributions
if want to use it at the commandline.


### Cool Penguin Demo

<p align="center">
	<img src="./cool-penguin.jpg"></img>
</div>


There is an image in this folder titled [`cool-penguin.jpg`](./cool-penguin.jpg).

One person will add this file to their local IPFS instance, and someone else will download it.

Once downloaded, the sender will then turn their computer off or simply disable the IPFS instance,
and somebody else will try to download it.

The content ID for this penguin is: `QmSKjMhnib5jFvQjpALfXxTNfjyN2uoN1veRXWmfJQRQQU`

#### Using the CLI

First, make sure to run `ipfs init` to initialize IPFS, and then `ipfs daemon`
to run your IPFS node. 

Then, in a separate tab, you can use the following IPFS commands:

To download the file in the CLI, simply enter `ipfs get QmSKjMhnib5jFvQjpALfXxTNfjyN2uoN1veRXWmfJQRQQU`

To add this file or another in the CLI, type `ipfs add path/to/file` and it will
be added to your node.

#### Using the Desktop

You should be able to download the file in the app by directly entering the content ID.

It should also provide you with an easy way to upload files directly through the UI.

