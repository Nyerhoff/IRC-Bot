##@file join.py
#@brief !join \<#channel\>+
#@author paullik
#@ingroup moduleFiles

import config

def join(components): # !join <#channel>+
    """Returns a string for joining the given channel(s)

    Joins a list of channels, only if the sender is an owner
    """

    response = ''

    join_command = components['arguments'].split('!join ')

    if 2 == len(join_command): #notice the space

        if components['sender'] in config.owner: #this command can be run only by the owner(s)
            response = []
            join_chans = []
            response.append('JOIN ')

            arg_channels = join_command[1].lstrip().split(' ')

            for channel in arg_channels:
                channel = channel.strip('\r')
                if channel not in config.channels and len(channel) and '#' == channel[0] \
                        and -1 == channel.find(' '): # valid channel name
                    join_chans.append(channel)
                    config.channels.append(channel)

            if len(join_chans):
                response.append(','.join(join_chans))
            else:
                response = 'Invalid channels names, usage: !join <#channel >+'

        else:
            response = 'This command can be run only by the owner(s)!'
    else:
        response = 'Usage: !join <#channel >+'

    return response
