########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

# built-in imports
import time

# other imports
from boto.ec2 import EC2Connection as EC2
from boto.exception import EC2ResponseError, BotoServerError

# Cloudify imports
<<<<<<< HEAD
from cloudify.exceptions import NonRecoverableError


def validate_state(instance, state, timeout_length, check_interval, ctx):
=======
from cloudify import ctx
from cloudify.exceptions import NonRecoverableError


def validate_state(instance, state, timeout_length, check_interval):
>>>>>>> ade788ef429d83ae3ffcbc79190ad883b01a4f5d
    """ Check if an EC2 instance is in a particular state.

    :param instance: And EC2 instance.
    :param state: The state code (pending = 0, running = 16,
                  shutting down = 32, terminated = 48, stopping = 64,
                  stopped = 80
    :param timeout_length: How long to wait for a positive answer
           before we stop checking.
    :param check_interval: How long to wait between checks.
    :return: bool (True the desired state was reached, False, it was not.)
    """

    ctx.logger.debug('(Node: {0}): Attempting state validation: '
                     'instance id: {0}, state: {1}, timeout length: {2}, '
                     'check interval: {3}.'.format(instance.id, state,
                                                   timeout_length,
                                                   check_interval))

    if check_interval < 1:
        check_interval = 1

    timeout = time.time() + timeout_length

    while True:
<<<<<<< HEAD
        if state == get_instance_state(instance, ctx=ctx):
=======
        if state == get_instance_state(instance):
>>>>>>> ade788ef429d83ae3ffcbc79190ad883b01a4f5d
            ctx.logger.info('(Node: {0}): '
                            'Instance state validated: instance {0}.'
                            .format(instance.state))
            return True
        elif time.time() > timeout:
            raise NonRecoverableError('(Node: {0}): Timed out during '
                                      'instance state validation: '
                                      'instance: {1}, '
                                      'timeout length: {2}, '
                                      'check interval: {3}.'
                                      .format(ctx.instance.id, instance.id,
                                              timeout_length,
                                              check_interval))
        time.sleep(check_interval)


def get_instance_state(instance, ctx):
    """

    :param instance:
    :return:
    """

    state = instance.update()
    ctx.logger.debug('(Node: {0}): Instance state is {1}.'
                     .format(ctx.instance.id, state))
    return instance.state_code


def validate_instance_id(instance_id, ctx):
    """

    :param instance_id: An EC2 instance ID
    :return: True that the instance ID is valid or
             throws unrecoverable error
    """

    try:
        reservations = EC2().get_all_reservations(instance_id)
    except (EC2ResponseError, BotoServerError) as e:
        raise NonRecoverableError('(Node: {0}): Error. '
                                  'Failed to validate instance id: '
                                  'API returned: {1}.'
                                  .format(ctx.instance.id, e))

    instance = reservations[0].instances[0]

    if instance:
        return True
    else:
        raise NonRecoverableError('(Node: {0}): Unable to validate '
                                  'instance ID: {1}.'
                                  .format(ctx.instance.id, instance_id))
<<<<<<< HEAD


def get_instance_from_id(instance_id, ctx):

    try:
        reservations = EC2().get_all_reservations(instance_id)
    except (EC2ResponseError, BotoServerError) as e:
        raise NonRecoverableError('(Node: {0}): Error. '
                                  'Failed to get instance by id: '
                                  'API returned: {1}.'
                                  .format(ctx.instance.id, e))

    instance = reservations[0].instances[0]

    return instance
=======
>>>>>>> ade788ef429d83ae3ffcbc79190ad883b01a4f5d