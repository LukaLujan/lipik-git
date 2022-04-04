# Neural Network with One Neuron 

For some reason, github didn't render whole code. In that case open this link;

https://nbviewer.org/github/LukaLujan/lipik-git/blob/master/simple_neuron.ipynb

Some time in late December 2021 I got in possession of one great book; Neural Networks from Scratch in Python by -Sentdex.

It took me a few weeks to grasp all new information, especially learning math like partial derivates , linear algebra, statistics etc. In following there is a full working  neural network that has only one neuron with all math behind it working like clockwork. 
Like in real life, it's starting parameters will be all random. It's first prediction will be way off from the our target value. However, we will use backpropagation with math so our neuron after each epoch will be updated with new better parameters (weight and biases) that should make after each epoch smaller and smaller loss (difference between predicted values and target values). After some amount of them , our neuron will find a "perfect" equation , where our "target value" will be equal (or almost equal) as "predicted value".
