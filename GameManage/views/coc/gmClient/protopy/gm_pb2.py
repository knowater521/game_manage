# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gm.proto',
  package='GM',
  serialized_pb='\n\x08gm.proto\x12\x02GM\"\xb0\x01\n\nbuild_info\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\x12\r\n\x05index\x18\x03 \x02(\x05\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\x12\x0e\n\x06\x66inish\x18\x06 \x02(\x05\x12\x13\n\x0bremain_time\x18\x07 \x01(\x05\x12\x13\n\x0btime_c_type\x18\x08 \x01(\x05\x12\x14\n\x0c\x63ollect_time\x18\t \x01(\x05\x12\x12\n\nbuild_time\x18\n \x01(\x05\"]\n\x04\x61rmy\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\x12\x10\n\x08\x63ounting\x18\x03 \x02(\x05\x12\x13\n\x0b\x63reate_time\x18\x04 \x02(\x05\x12\x13\n\x0bremain_time\x18\x05 \x02(\x05\"b\n\tarmy_info\x12\r\n\x05index\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x02(\x05\x12\x11\n\tsum_count\x18\x03 \x02(\x05\x12\x0e\n\x06\x66inish\x18\x04 \x02(\x05\x12\x17\n\x05\x61rmys\x18\x05 \x03(\x0b\x32\x08.GM.army\"$\n\x07\x61rmy_lv\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\"\x8d\x02\n\trole_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05level\x18\x02 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x02(\x05\x12\x0e\n\x06points\x18\x04 \x02(\x05\x12\x0b\n\x03gem\x18\x05 \x02(\x05\x12\x10\n\x08goldcoin\x18\x06 \x02(\x05\x12\x14\n\x0cmax_goldcoin\x18\x07 \x02(\x05\x12\r\n\x05water\x18\x08 \x02(\x05\x12\x11\n\tmax_water\x18\t \x02(\x05\x12\x13\n\x0b\x62uild_count\x18\n \x02(\x05\x12\x1e\n\x06\x62uilds\x18\x0b \x03(\x0b\x32\x0e.GM.build_info\x12\x1c\n\x05\x61rmys\x18\x0c \x03(\x0b\x32\r.GM.army_info\x12\x1c\n\x07\x61rmylvs\x18\r \x03(\x0b\x32\x0b.GM.army_lv\"\'\n\x12QueryPlayerDataReq\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\"[\n\x12QueryPlayerDataRsp\x12\x0e\n\x06result\x18\x01 \x02(\x05\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\"\n\x0bplayer_data\x18\x03 \x01(\x0b\x32\r.GM.role_info\"\xb7\x01\n\x13ModifyPlayerDataReq\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\x12\x0c\n\x04\x66lag\x18\x02 \x02(\x05\x12\x14\n\x0cwater_change\x18\x03 \x01(\x05\x12\x17\n\x0fgoldcoin_change\x18\x04 \x01(\x05\x12\x12\n\ngem_change\x18\x05 \x01(\x05\x12\x12\n\nlvl_change\x18\x06 \x01(\x05\x12\x12\n\nexp_change\x18\x07 \x01(\x05\x12\x14\n\x0cpoint_change\x18\x08 \x01(\x05\"O\n\x13ModifyPlayerDataRsp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12&\n\x0fnew_player_data\x18\x02 \x01(\x0b\x32\r.GM.role_info')




_BUILD_INFO = _descriptor.Descriptor(
  name='build_info',
  full_name='GM.build_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GM.build_info.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GM.build_info.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='GM.build_info.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='GM.build_info.x', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='GM.build_info.y', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish', full_name='GM.build_info.finish', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='GM.build_info.remain_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_c_type', full_name='GM.build_info.time_c_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collect_time', full_name='GM.build_info.collect_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_time', full_name='GM.build_info.build_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=193,
)


_ARMY = _descriptor.Descriptor(
  name='army',
  full_name='GM.army',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GM.army.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='GM.army.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counting', full_name='GM.army.counting', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='GM.army.create_time', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='GM.army.remain_time', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=195,
  serialized_end=288,
)


_ARMY_INFO = _descriptor.Descriptor(
  name='army_info',
  full_name='GM.army_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='GM.army_info.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='GM.army_info.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sum_count', full_name='GM.army_info.sum_count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish', full_name='GM.army_info.finish', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armys', full_name='GM.army_info.armys', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=290,
  serialized_end=388,
)


_ARMY_LV = _descriptor.Descriptor(
  name='army_lv',
  full_name='GM.army_lv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GM.army_lv.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GM.army_lv.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=390,
  serialized_end=426,
)


_ROLE_INFO = _descriptor.Descriptor(
  name='role_info',
  full_name='GM.role_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='GM.role_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GM.role_info.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='GM.role_info.exp', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='GM.role_info.points', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem', full_name='GM.role_info.gem', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goldcoin', full_name='GM.role_info.goldcoin', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_goldcoin', full_name='GM.role_info.max_goldcoin', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='water', full_name='GM.role_info.water', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_water', full_name='GM.role_info.max_water', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_count', full_name='GM.role_info.build_count', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builds', full_name='GM.role_info.builds', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armys', full_name='GM.role_info.armys', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armylvs', full_name='GM.role_info.armylvs', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=429,
  serialized_end=698,
)


_QUERYPLAYERDATAREQ = _descriptor.Descriptor(
  name='QueryPlayerDataReq',
  full_name='GM.QueryPlayerDataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='GM.QueryPlayerDataReq.player_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=700,
  serialized_end=739,
)


_QUERYPLAYERDATARSP = _descriptor.Descriptor(
  name='QueryPlayerDataRsp',
  full_name='GM.QueryPlayerDataRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GM.QueryPlayerDataRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='GM.QueryPlayerDataRsp.player_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_data', full_name='GM.QueryPlayerDataRsp.player_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=741,
  serialized_end=832,
)


_MODIFYPLAYERDATAREQ = _descriptor.Descriptor(
  name='ModifyPlayerDataReq',
  full_name='GM.ModifyPlayerDataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='GM.ModifyPlayerDataReq.player_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='GM.ModifyPlayerDataReq.flag', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='water_change', full_name='GM.ModifyPlayerDataReq.water_change', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goldcoin_change', full_name='GM.ModifyPlayerDataReq.goldcoin_change', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem_change', full_name='GM.ModifyPlayerDataReq.gem_change', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lvl_change', full_name='GM.ModifyPlayerDataReq.lvl_change', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp_change', full_name='GM.ModifyPlayerDataReq.exp_change', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_change', full_name='GM.ModifyPlayerDataReq.point_change', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=835,
  serialized_end=1018,
)


_MODIFYPLAYERDATARSP = _descriptor.Descriptor(
  name='ModifyPlayerDataRsp',
  full_name='GM.ModifyPlayerDataRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='GM.ModifyPlayerDataRsp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_player_data', full_name='GM.ModifyPlayerDataRsp.new_player_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1020,
  serialized_end=1099,
)

_ARMY_INFO.fields_by_name['armys'].message_type = _ARMY
_ROLE_INFO.fields_by_name['builds'].message_type = _BUILD_INFO
_ROLE_INFO.fields_by_name['armys'].message_type = _ARMY_INFO
_ROLE_INFO.fields_by_name['armylvs'].message_type = _ARMY_LV
_QUERYPLAYERDATARSP.fields_by_name['player_data'].message_type = _ROLE_INFO
_MODIFYPLAYERDATARSP.fields_by_name['new_player_data'].message_type = _ROLE_INFO
DESCRIPTOR.message_types_by_name['build_info'] = _BUILD_INFO
DESCRIPTOR.message_types_by_name['army'] = _ARMY
DESCRIPTOR.message_types_by_name['army_info'] = _ARMY_INFO
DESCRIPTOR.message_types_by_name['army_lv'] = _ARMY_LV
DESCRIPTOR.message_types_by_name['role_info'] = _ROLE_INFO
DESCRIPTOR.message_types_by_name['QueryPlayerDataReq'] = _QUERYPLAYERDATAREQ
DESCRIPTOR.message_types_by_name['QueryPlayerDataRsp'] = _QUERYPLAYERDATARSP
DESCRIPTOR.message_types_by_name['ModifyPlayerDataReq'] = _MODIFYPLAYERDATAREQ
DESCRIPTOR.message_types_by_name['ModifyPlayerDataRsp'] = _MODIFYPLAYERDATARSP

class build_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUILD_INFO

  # @@protoc_insertion_point(class_scope:GM.build_info)

class army(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY

  # @@protoc_insertion_point(class_scope:GM.army)

class army_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY_INFO

  # @@protoc_insertion_point(class_scope:GM.army_info)

class army_lv(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARMY_LV

  # @@protoc_insertion_point(class_scope:GM.army_lv)

class role_info(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLE_INFO

  # @@protoc_insertion_point(class_scope:GM.role_info)

class QueryPlayerDataReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYPLAYERDATAREQ

  # @@protoc_insertion_point(class_scope:GM.QueryPlayerDataReq)

class QueryPlayerDataRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYPLAYERDATARSP

  # @@protoc_insertion_point(class_scope:GM.QueryPlayerDataRsp)

class ModifyPlayerDataReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODIFYPLAYERDATAREQ

  # @@protoc_insertion_point(class_scope:GM.ModifyPlayerDataReq)

class ModifyPlayerDataRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODIFYPLAYERDATARSP

  # @@protoc_insertion_point(class_scope:GM.ModifyPlayerDataRsp)


# @@protoc_insertion_point(module_scope)