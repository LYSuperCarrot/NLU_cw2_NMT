import torch.nn as nn


class Seq2SeqModel(nn.Module):
    def __init__(self, encoder, decoder):
        super().__init__()
        assert isinstance(encoder, Seq2SeqEncoder)   # isinstance() 函数来判断一个对象是否是一个已知的类型，考虑继承关系
        assert isinstance(decoder, Seq2SeqDecoder)   # Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常
        self.encoder = encoder
        self.decoder = decoder

    @staticmethod
    def add_args(parser):
        """Add model-specific arguments to the parser."""
        pass

    @classmethod
    def build_model(cls, args, src_dict, tgt_dict):
        """Build a new model instance."""
        raise NotImplementedError

    def forward(self, src_tokens, src_lengths, tgt_inputs):
        encoder_out = self.encoder(src_tokens, src_lengths)
        decoder_out = self.decoder(tgt_inputs, encoder_out)
        return decoder_out


class Seq2SeqEncoder(nn.Module):
    def __init__(self, dictionary):
        super().__init__()
        self.dictionary = dictionary

    def forward(self, src_tokens, src_lengths):
        raise NotImplementedError


class Seq2SeqDecoder(nn.Module):
    def __init__(self, dictionary):
        super().__init__()
        self.dictionary = dictionary

    def forward(self, src_inputs, tgt_inputs, encoder_out):
        raise NotImplementedError
