local args = require 'common.args'
local class = require 'common.class'
local helpers = require 'common.helpers'
local log = require 'common.log'
local events = require 'system.events'
local random = require 'system.random'
local tensor = require 'system.tensor'

local meltingpot = 'meltingpot.lua.modules.'
local component = require(meltingpot .. 'component')
local component_registry = require(meltingpot .. 'component_registry')

local _COMPASS = {'N', 'E', 'S', 'W'}

local PickUp = class.Class(component.Component)

function PickUp:__init__(kwargs)
  kwargs = args.parse(kwargs, {
      {'name', args.default('PickUp')},
      {'idx', args.numberType},
  })
  PickUp.Base.__init__(self, kwargs)
  self._idx = kwargs.idx
end

function PickUp:onEnter(enteringGameObject, contactName)
  if contactName == 'avatar' then
--     if self.gameObject:getState() == self._liveState then
      local sequentialCollection = enteringGameObject:getComponent('SequentialCollection')
      -- Reward the player if collected in correct sequence
      if self._idx == sequentialCollection:getTarget() then
        local avatarComponent = enteringGameObject:getComponent('Avatar')
    --         avatarComponent:addReward(self._config.rewardForEating)
        avatarComponent:addReward(5)
        if sequentialCollection:getTarget() < 3 then
          sequentialCollection:incrementTarget()
        else
          sequentialCollection:reset()
        end
      else
        sequentialCollection:reset()
      end
--     end
  end
end


local SequentialCollection = class.Class(component.Component)

function SequentialCollection:__init__(kwargs)
    kwargs = args.parse(kwargs, {
        {'name', args.default('SequentialCollection')},
        {'sequence', args.default({1, 2, 3}), args.tableType},
    })
    SequentialCollection.Base.__init__(self, kwargs)
    self._sequence = kwargs.sequence
end

function SequentialCollection:reset()
    self._idx = 1
end

function SequentialCollection:getTarget()
    return self._idx
end

function SequentialCollection:incrementTarget()
    self._idx = self._idx + 1
end

local allComponents = {
    PickUp = PickUp,
    SequentialCollection = SequentialCollection,
}
component_registry.registerAllComponents(allComponents)

return allComponents